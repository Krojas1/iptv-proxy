import re
import os
from flask import Flask, redirect, Response
import requests

app = Flask(__name__)

# Base de la URL de origen de los canales
BASE_API_URL = "https://streamtp99a.sbs"
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'

@app.route('/canal/<nombre_canal>')
def get_stream(nombre_canal):
    try:
        # 1. Construye dinámicamente la URL (ej: .../global1.php?stream=espn2)
        url_objetivo = f"{BASE_API_URL}{nombre_canal}"
        
        headers = {'User-Agent': USER_AGENT}
        response = requests.get(url_objetivo, headers=headers, timeout=10)
        
        # 2. Expresión regular universal para capturar cualquier dominio de transmisión (s8, s9, s10, etc.)
        match = re.search(r'(https://[a-zA-Z0-9.-]+\.xyz/[a-zA-Z0-9._-]+/.*?\.m3u8\?ip=.*?&token=[a-zA-Z0-9-]+)', response.text)
        
        if match:
            real_stream_url = match.group(1)
            # 3. Redirección HTTP 302 directa a tu app de IPTV
            return redirect(real_stream_url, code=302)
            
    except Exception as e:
        print(f"Error al procesar el canal {nombre_canal}: {e}")
        
    return Response(f"Canal '{nombre_canal}' no disponible o no encontrado.", status=404)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
