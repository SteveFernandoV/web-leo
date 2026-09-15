const FIREBASE_API_KEY = 'AIzaSyDeWp7TBvy5CAiTFCZToA6JEsK8xL3NVoQ';

export async function requireAdmin(req) {
  const authorization = req.headers.authorization || '';
  const idToken = authorization.startsWith('Bearer ') ? authorization.slice(7) : '';

  if (!idToken) {
    return { ok: false, status: 401, message: 'Debes iniciar sesión para administrar fotografías.' };
  }

  const response = await fetch(
    `https://identitytoolkit.googleapis.com/v1/accounts:lookup?key=${FIREBASE_API_KEY}`,
    {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ idToken })
    }
  );

  if (!response.ok) {
    return { ok: false, status: 401, message: 'La sesión administrativa venció. Vuelve a ingresar.' };
  }

  const payload = await response.json();
  const user = payload.users?.[0];
  const configuredEmail = (process.env.FIREBASE_ADMIN_EMAIL || '').trim().toLowerCase();
  const userEmail = (user?.email || '').trim().toLowerCase();

  if (!configuredEmail) {
    return { ok: false, status: 503, message: 'El administrador todavía no está configurado en Vercel.' };
  }

  if (!user || !userEmail || userEmail !== configuredEmail) {
    return { ok: false, status: 403, message: 'Esta cuenta no tiene permisos de propietario.' };
  }

  return { ok: true, user };
}

export function sendJson(res, status, body) {
  res.status(status);
  res.setHeader('content-type', 'application/json; charset=utf-8');
  res.setHeader('cache-control', 'no-store');
  res.json(body);
}
