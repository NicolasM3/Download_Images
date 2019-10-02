from google_images_download import google_images_download   # * livrarias
import sys

# * argumentos necessários
busca = input("Termo a pesquisar: ")    
limit = input("quantidade a pesquisar: ")
formato = input("formato desejado: (jpg, gif, png, bmp, svg, webp, ico, raw) ")

response = google_images_download.googleimagesdownload()   # * instanciação da classe

# * argumentos
arguments = {"keywords":busca,"limit":limit, "print_urls":True, "delay":1,
             "output_directory":"imagens", "prefix":busca, "format":formato}
paths = response.download(arguments)    # * passandos os argumentos para a função
print(paths)