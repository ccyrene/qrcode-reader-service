import io
import time
import uvicorn

from fastapi import FastAPI, Request
from fastapi.responses import Response

from argparses import get_args
from qrlib import generate_qr_code

app = FastAPI()

@app.post("/generateQRCode")
async def generate_qr(request: Request):
    
    start_all_time = time.time()
    
    start_time = time.time()
    request = await request.json()
    print(f"wait request: {(time.time() - start_time)*1000:.2f} ms") 
    
    start_time = time.time()
    qr_img = generate_qr_code(request["uuid"])
    print(f"generate QR code: {(time.time() - start_time)*1000:.2f} ms")

    start_time = time.time()
    img_byte_arr = io.BytesIO()
    qr_img.save(img_byte_arr, format="PNG")
    img_byte_arr = img_byte_arr.getvalue()
    print(f"convert Image to Bytes: {(time.time() - start_time)*1000:.2f} ms")
    
    print(f"Precise Time: {(time.time() - start_all_time)*1000:.2f} ms")
    return Response(content=img_byte_arr, media_type="image/png")

if __name__ == "__main__":

    args = get_args()
    uvicorn.run("app:app", host="0.0.0.0", port=args.port, loop="uvloop", workers=args.workers)