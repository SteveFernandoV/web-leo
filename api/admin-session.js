import { requireAdmin, sendJson } from './_firebase-admin.js';

export default async function handler(req, res) {
  if (req.method !== 'GET') {
    res.setHeader('allow', 'GET');
    return sendJson(res, 405, { ok: false, message: 'Método no permitido.' });
  }

  try {
    const auth = await requireAdmin(req);
    if (!auth.ok) return sendJson(res, auth.status, { ok: false, message: auth.message });
    return sendJson(res, 200, {
      ok: true,
      user: {
        displayName: auth.user.displayName || 'Propietario',
        email: auth.user.email
      }
    });
  } catch (error) {
    console.error('admin-session', error);
    return sendJson(res, 500, { ok: false, message: 'No se pudo validar la cuenta administrativa.' });
  }
}
