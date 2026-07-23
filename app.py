import re
import os
from flask import Flask, redirect, Response
import requests

app = Flask(__name__)

BASE_API_URL = "https://streamtp99a.sbs"

@app.route('/canal/<nombre_canal>')
def get_stream(nombre_canal):
    try:
        url_objetivo = f"{BASE_API_URL}{nombre_canal}"
        
        # Cabeceras avanzadas para engañar al sistema y simular una pestaña real
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'es-ES,es;q=0.9',
            'Referer': 'https://todopelota.su',
            'Origin': 'https://todopelota.su'
        }
        
        # Realizar la petición usando un tiempo de espera de 8 segundos
        response = requests.get(url_objetivo, headers=headers, timeout=8)
        
        # Buscar la URL .m3u8 con su token vigente
        match = re.search(r'(https://[a-zA-Z0-9.-]+\.xyz/[a-zA-Z0-9._-]+/.*?\.m3u8\?ip=.*?&token=[a-zA-Z0-9-]+)', response.text)
        
        if match:
            real_stream_url = match.group(1)
            # Redirección directa hacia el reproductor IPTV
            return redirect(real_stream_url, code=302)
            
    except Exception as e:
        print(f"Error en canal {nombre_canal}: {e}")
        
    return Response(f"Canal '{nombre_canal}' bloqueado o no disponible temporalmente.", status=404)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
