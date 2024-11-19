import requests
from bs4 import BeautifulSoup

# URL do site para scraping
url = "https://books.toscrape.com/catalogue/page-1.html"

# Função para realizar o scraping
def scrape_books(url):
    # Envia uma solicitação HTTP para o site
    response = requests.get(url)
    
    # Verifica se a solicitação foi bem-sucedida
    if response.status_code != 200:
        print("Erro ao acessar a página:", response.status_code)
        return
    
    # Analisa o conteúdo HTML da página
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Encontra os blocos de livros na página
    books = soup.find_all("article", class_="product_pod")
    
    # Lista para armazenar informações dos livros
    book_data = []
    
    for book in books:
        # Extrai o título do livro
        title = book.h3.a["title"]
        
        # Extrai o preço do livro
        price = book.find("p", class_="price_color").text.strip()
        
        # Extrai a disponibilidade do livro
        availability = book.find("p", class_="instock availability").text.strip()
        
        # Adiciona as informações à lista
        book_data.append({
            "title": title,
            "price": price,
            "availability": availability
        })
    
    # Exibe os dados coletados
    for book in book_data:
        print(f"Título: {book['title']}")
        print(f"Preço: {book['price']}")
        print(f"Disponibilidade: {book['availability']}")
        print("-" * 40)

# Executa o scraping
scrape_books(url)
