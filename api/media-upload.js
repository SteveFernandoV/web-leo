import { put } from '@vercel/blob';
import { requireAdmin, sendJson } from './_firebase-admin.js';

const MAX_FILE_BYTES = 4 * 1024 * 1024;
const ALLOWED_TYPES = new Set(['image/jpeg', 'image/png', 'image/webp', 'image/gif']);

function readBody(req) {
  return new Promise((resolve, reject) => {
    const chunks = [];
    let size = 0;

    req.on('data', (chunk) => {
      size += chunk.length;
      if (size > MAX_FILE_BYTES) {
        reject(new Error('FILE_TOO_LARGE'));
        req.destroy();
        return;
      }
      chunks.push(chunk);
    });
    req.on('end', () => resolve(Buffer.concat(chunks)));
    req.on('error', reject);
  });
}

function safeSegment(value, fallback) {
  const normalized = String(value || '')
    .normalize('NFKD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .replace(/[^a-z0-9._-]+/g, '-')
    .replace(/^-+|-+$/g, '')
    .slice(0, 80);
  return normalized || fallback;
}

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('allow', 'POST');
    return sendJson(res, 405, { ok: false, message: 'Método no permitido.' });
  }

  try {
    const auth = await requireAdmin(req);
    if (!auth.ok) return sendJson(res, auth.status, { ok: false, message: auth.message });

    const contentType = String(req.headers['content-type'] || '').split(';')[0].toLowerCase();
    if (!ALLOWED_TYPES.has(contentType)) {
      return sendJson(res, 415, { ok: false, message: 'Formato no permitido. Usa JPG, PNG, WebP o GIF.' });
    }

    const body = await readBody(req);
    if (!body.length) return sendJson(res, 400, { ok: false, message: 'La imagen está vacía.' });

    const section = safeSegment(req.query.section, 'general');
    const filename = safeSegment(req.headers['x-file-name'], 'imagen.jpg');
    const pathname = `happy-tactical/${section}/${Date.now()}-${filename}`;
    const blob = await put(pathname, body, {
      access: 'public',
      addRandomSuffix: true,
      contentType,
      cacheControlMaxAge: 31536000
    });

    return sendJson(res, 201, {
      ok: true,
      url: blob.url,
      pathname: blob.pathname,
      contentType
    });
  } catch (error) {
    const tooLarge = error?.message === 'FILE_TOO_LARGE';
    console.error('media-upload', tooLarge ? 'file-too-large' : error);
    return sendJson(res, tooLarge ? 413 : 500, {
      ok: false,
      message: tooLarge
        ? 'La imagen supera el límite de 4 MB después de optimizarse.'
        : 'No se pudo publicar la imagen. Inténtalo nuevamente.'
    });
  }
}

export const config = {
  api: { bodyParser: false }
};
