import { del } from '@vercel/blob';
import { requireAdmin, sendJson } from './_firebase-admin.js';

export default async function handler(req, res) {
  if (req.method !== 'DELETE') {
    res.setHeader('allow', 'DELETE');
    return sendJson(res, 405, { ok: false, message: 'Método no permitido.' });
  }

  try {
    const auth = await requireAdmin(req);
    if (!auth.ok) return sendJson(res, auth.status, { ok: false, message: auth.message });

    const url = String(req.query.url || '');
    let parsedUrl;
    try {
      parsedUrl = new URL(url);
    } catch {
      parsedUrl = null;
    }
    if (!parsedUrl || parsedUrl.protocol !== 'https:' || !parsedUrl.hostname.endsWith('.public.blob.vercel-storage.com')) {
      return sendJson(res, 400, { ok: false, message: 'Dirección de imagen inválida.' });
    }

    await del(url);
    return sendJson(res, 200, { ok: true });
  } catch (error) {
    console.error('media-delete', error);
    return sendJson(res, 500, { ok: false, message: 'No se pudo eliminar el archivo almacenado.' });
  }
}
