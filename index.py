import qrcode
import qrcode.constants

# Configuração do QR Code
qr = qrcode.QRCode(
    version=1,  # Tamanho do QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nível de correção de erros
    box_size=20,  # Tamanho de cada caixa do QR Code
    border=2  # Tamanho da borda
)

# Adiciona dados ao QR Code
qr.add_data("https://github.com/ViniciusAlexandrino?tab=repositories")

# Gera o QR Code
qr.make(fit=True)

# Cria a imagem do QR Code
img = qr.make_image(fill_color="black", back_color="white")

# Salva a imagem
img.save("qr.png")
