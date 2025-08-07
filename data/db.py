from datetime import datetime
from typing import Any, Dict, List, Optional


class BookDatabase:
    def __init__(self):
        self.books = {
            "angelologia": {
                "id": "angelologia",
                "title": "Curso Teológico - Angelologia",
                "author": "Pastor Paulo Coutinho",
                "type": "ebook",
                "price": 10.00,
                "rating": 4.9,
                "reviews": 12540,
                "description": "Curso criado pelo Pastor e Mestre em História da Igreja, Paulo Coutinho. Metodologias acadêmicas para produzir material de estudo, como regras ABNT. Material colorido, padronizado, com referências bibliográficas, tabelas, ilustrações e muito mais. Usado e aprovado em cursos de teologia.",
                "category": "Teologia Sistemática",
                "pages": 120,
                "language": "Português",
                "format": "PDF",
                "popularity": 98,
            },
            "antigo_testamento": {
                "id": "antigo_testamento",
                "title": "Curso Teológico - Antigo Testamento",
                "author": "Pastor Paulo Coutinho",
                "type": "ebook",
                "price": 10.00,
                "rating": 4.8,
                "reviews": 8920,
                "description": "Curso criado pelo Pastor e Mestre em História da Igreja, Paulo Coutinho. Metodologias acadêmicas para produzir material de estudo, como regras ABNT. Material colorido, padronizado, com referências bibliográficas, tabelas, ilustrações e muito mais. Usado e aprovado em cursos de teologia.",
                "category": "Estudo Bíblico",
                "pages": 150,
                "language": "Português",
                "format": "PDF",
                "popularity": 95,
            },
            "bibliologia": {
                "id": "bibliologia",
                "title": "Curso Teológico - Bibliologia",
                "author": "Pastor Paulo Coutinho",
                "type": "ebook",
                "price": 10.00,
                "rating": 4.7,
                "reviews": 5670,
                "description": "Curso criado pelo Pastor e Mestre em História da Igreja, Paulo Coutinho. Metodologias acadêmicas para produzir material de estudo, como regras ABNT. Material colorido, padronizado, com referências bibliográficas, tabelas, ilustrações e muito mais. Usado e aprovado em cursos de teologia.",
                "category": "Teologia Sistemática",
                "pages": 100,
                "language": "Português",
                "format": "PDF",
                "popularity": 88,
            },
            "cristologia": {
                "id": "cristologia",
                "title": "Curso Teológico - Cristologia",
                "author": "Pastor Paulo Coutinho",
                "type": "ebook",
                "price": 10.00,
                "rating": 4.9,
                "reviews": 12340,
                "description": "Curso criado pelo Pastor e Mestre em História da Igreja, Paulo Coutinho. Metodologias acadêmicas para produzir material de estudo, como regras ABNT. Material colorido, padronizado, com referências bibliográficas, tabelas, ilustrações e muito mais. Usado e aprovado em cursos de teologia.",
                "category": "Teologia Sistemática",
                "pages": 140,
                "language": "Português",
                "format": "PDF",
                "popularity": 96,
            },
            "escatologia": {
                "id": "escatologia",
                "title": "Curso Teológico - Escatologia",
                "author": "Pastor Paulo Coutinho",
                "type": "ebook",
                "price": 10.00,
                "rating": 4.6,
                "reviews": 4450,
                "description": "Curso criado pelo Pastor e Mestre em História da Igreja, Paulo Coutinho. Metodologias acadêmicas para produzir material de estudo, como regras ABNT. Material colorido, padronizado, com referências bibliográficas, tabelas, ilustrações e muito mais. Usado e aprovado em cursos de teologia.",
                "category": "Teologia Sistemática",
                "pages": 130,
                "language": "Português",
                "format": "PDF",
                "popularity": 82,
            },
            "evangelismo_missoes": {
                "id": "evangelismo_missoes",
                "title": "Curso Teológico - Evangelismo e Missões",
                "author": "Pastor Paulo Coutinho",
                "type": "ebook",
                "price": 10.00,
                "rating": 4.7,
                "reviews": 5670,
                "description": "Curso criado pelo Pastor e Mestre em História da Igreja, Paulo Coutinho. Metodologias acadêmicas para produzir material de estudo, como regras ABNT. Material colorido, padronizado, com referências bibliográficas, tabelas, ilustrações e muito mais. Usado e aprovado em cursos de teologia.",
                "category": "Ministério Prático",
                "pages": 110,
                "language": "Português",
                "format": "PDF",
                "popularity": 84,
            },
            "exegese": {
                "id": "exegese",
                "title": "Curso Teológico - Exegese",
                "author": "Pastor Paulo Coutinho",
                "type": "ebook",
                "price": 10.00,
                "rating": 4.8,
                "reviews": 7890,
                "description": "Curso criado pelo Pastor e Mestre em História da Igreja, Paulo Coutinho. Metodologias acadêmicas para produzir material de estudo, como regras ABNT. Material colorido, padronizado, com referências bibliográficas, tabelas, ilustrações e muito mais. Usado e aprovado em cursos de teologia.",
                "category": "Hermenêutica",
                "pages": 125,
                "language": "Português",
                "format": "PDF",
                "popularity": 90,
            },
            "geografia_biblica": {
                "id": "geografia_biblica",
                "title": "Curso Teológico - Geografia Bíblica",
                "author": "Pastor Paulo Coutinho",
                "type": "ebook",
                "price": 10.00,
                "rating": 4.5,
                "reviews": 3890,
                "description": "Curso criado pelo Pastor e Mestre em História da Igreja, Paulo Coutinho. Metodologias acadêmicas para produzir material de estudo, como regras ABNT. Material colorido, padronizado, com referências bibliográficas, tabelas, ilustrações e muito mais. Usado e aprovado em cursos de teologia.",
                "category": "Estudo Bíblico",
                "pages": 95,
                "language": "Português",
                "format": "PDF",
                "popularity": 78,
            },
            "hamartiologia": {
                "id": "hamartiologia",
                "title": "Curso Teológico - Hamartiologia",
                "author": "Pastor Paulo Coutinho",
                "type": "ebook",
                "price": 10.00,
                "rating": 4.7,
                "reviews": 6340,
                "description": "Curso criado pelo Pastor e Mestre em História da Igreja, Paulo Coutinho. Metodologias acadêmicas para produzir material de estudo, como regras ABNT. Material colorido, padronizado, com referências bibliográficas, tabelas, ilustrações e muito mais. Usado e aprovado em cursos de teologia.",
                "category": "Teologia Sistemática",
                "pages": 105,
                "language": "Português",
                "format": "PDF",
                "popularity": 85,
            },
            "hermeneutica": {
                "id": "hermeneutica",
                "title": "Curso Teológico - Hermenêutica",
                "author": "Pastor Paulo Coutinho",
                "type": "ebook",
                "price": 10.00,
                "rating": 4.8,
                "reviews": 7230,
                "description": "Curso criado pelo Pastor e Mestre em História da Igreja, Paulo Coutinho. Metodologias acadêmicas para produzir material de estudo, como regras ABNT. Material colorido, padronizado, com referências bibliográficas, tabelas, ilustrações e muito mais. Usado e aprovado em cursos de teologia.",
                "category": "Hermenêutica",
                "pages": 115,
                "language": "Português",
                "format": "PDF",
                "popularity": 89,
            },
            "historia_cultura_judaica": {
                "id": "historia_cultura_judaica",
                "title": "Curso Teológico - História e Cultura Judaica",
                "author": "Pastor Paulo Coutinho",
                "type": "ebook",
                "price": 10.00,
                "rating": 4.6,
                "reviews": 4560,
                "description": "Curso criado pelo Pastor e Mestre em História da Igreja, Paulo Coutinho. Metodologias acadêmicas para produzir material de estudo, como regras ABNT. Material colorido, padronizado, com referências bibliográficas, tabelas, ilustrações e muito mais. Usado e aprovado em cursos de teologia.",
                "category": "História",
                "pages": 135,
                "language": "Português",
                "format": "PDF",
                "popularity": 80,
            },
            "historia_da_igreja": {
                "id": "historia_da_igreja",
                "title": "Curso Teológico - História da Igreja",
                "author": "Pastor Paulo Coutinho",
                "type": "ebook",
                "price": 10.00,
                "rating": 4.9,
                "reviews": 9870,
                "description": "Curso criado pelo Pastor e Mestre em História da Igreja, Paulo Coutinho. Metodologias acadêmicas para produzir material de estudo, como regras ABNT. Material colorido, padronizado, com referências bibliográficas, tabelas, ilustrações e muito mais. Usado e aprovado em cursos de teologia.",
                "category": "História",
                "pages": 180,
                "language": "Português",
                "format": "PDF",
                "popularity": 94,
            },
            "homiletica": {
                "id": "homiletica",
                "title": "Curso Teológico - Homilética",
                "author": "Pastor Paulo Coutinho",
                "type": "ebook",
                "price": 10.00,
                "rating": 4.7,
                "reviews": 6780,
                "description": "Curso criado pelo Pastor e Mestre em História da Igreja, Paulo Coutinho. Metodologias acadêmicas para produzir material de estudo, como regras ABNT. Material colorido, padronizado, com referências bibliográficas, tabelas, ilustrações e muito mais. Usado e aprovado em cursos de teologia.",
                "category": "Ministério Prático",
                "pages": 120,
                "language": "Português",
                "format": "PDF",
                "popularity": 87,
            },
            "novo_testamento": {
                "id": "novo_testamento",
                "title": "Curso Teológico - Novo Testamento",
                "author": "Pastor Paulo Coutinho",
                "type": "ebook",
                "price": 10.00,
                "rating": 4.8,
                "reviews": 8230,
                "description": "Curso criado pelo Pastor e Mestre em História da Igreja, Paulo Coutinho. Metodologias acadêmicas para produzir material de estudo, como regras ABNT. Material colorido, padronizado, com referências bibliográficas, tabelas, ilustrações e muito mais. Usado e aprovado em cursos de teologia.",
                "category": "Estudo Bíblico",
                "pages": 160,
                "language": "Português",
                "format": "PDF",
                "popularity": 92,
            },
            "vale_de_ela": {
                "id": "vale_de_ela",
                "title": "O Vale de Elá - Quando Deus Planta em Vales",
                "author": "Pastor Paulo Coutinho",
                "type": "ebook",
                "price": 10.00,
                "rating": 4.9,
                "reviews": 11230,
                "description": "Uma jornada profunda através do Vale de Elá, onde a fé enfrenta o medo e a vitória nasce da dependência em Deus. Análise detalhada do significado espiritual do nome Elá e sua conexão com a árvore terebinto, símbolo de resistência e regeneração. Estudo completo da batalha entre Davi e Golias, revelando as dimensões espirituais que vão muito além do confronto físico.",
                "category": "Estudo Bíblico",
                "pages": 200,
                "language": "Português",
                "format": "PDF",
                "popularity": 97,
            },
            "pneumatologia": {
                "id": "pneumatologia",
                "title": "Curso Teológico - Pneumatologia",
                "author": "Pastor Paulo Coutinho",
                "type": "ebook",
                "price": 10.00,
                "rating": 4.6,
                "reviews": 5120,
                "description": "Curso criado pelo Pastor e Mestre em História da Igreja, Paulo Coutinho. Metodologias acadêmicas para produzir material de estudo, como regras ABNT. Material colorido, padronizado, com referências bibliográficas, tabelas, ilustrações e muito mais. Usado e aprovado em cursos de teologia.",
                "category": "Teologia Sistemática",
                "pages": 125,
                "language": "Português",
                "format": "PDF",
                "popularity": 83,
            },
            "religioes_seitas_heresias": {
                "id": "religioes_seitas_heresias",
                "title": "Curso Teológico - Religiões, Seitas e Heresias",
                "author": "Pastor Paulo Coutinho",
                "type": "ebook",
                "price": 10.00,
                "rating": 4.5,
                "reviews": 4230,
                "description": "Curso criado pelo Pastor e Mestre em História da Igreja, Paulo Coutinho. Metodologias acadêmicas para produzir material de estudo, como regras ABNT. Material colorido, padronizado, com referências bibliográficas, tabelas, ilustrações e muito mais. Usado e aprovado em cursos de teologia.",
                "category": "Apologética",
                "pages": 140,
                "language": "Português",
                "format": "PDF",
                "popularity": 79,
            },
            "soteriologia_eclesiologia": {
                "id": "soteriologia_eclesiologia",
                "title": "Curso Teológico - Soteriologia e Eclesiologia",
                "author": "Pastor Paulo Coutinho",
                "type": "ebook",
                "price": 10.00,
                "rating": 4.7,
                "reviews": 6540,
                "description": "Curso criado pelo Pastor e Mestre em História da Igreja, Paulo Coutinho. Metodologias acadêmicas para produzir material de estudo, como regras ABNT. Material colorido, padronizado, com referências bibliográficas, tabelas, ilustrações e muito mais. Usado e aprovado em cursos de teologia.",
                "category": "Teologia Sistemática",
                "pages": 155,
                "language": "Português",
                "format": "PDF",
                "popularity": 86,
            },
            "teologia_propria": {
                "id": "teologia_propria",
                "title": "Curso Teológico - Teologia Própria - Teontologia",
                "author": "Pastor Paulo Coutinho",
                "type": "ebook",
                "price": 10.00,
                "rating": 4.8,
                "reviews": 7450,
                "description": "Curso criado pelo Pastor e Mestre em História da Igreja, Paulo Coutinho. Metodologias acadêmicas para produzir material de estudo, como regras ABNT. Material colorido, padronizado, com referências bibliográficas, tabelas, ilustrações e muito mais. Usado e aprovado em cursos de teologia.",
                "category": "Teologia Sistemática",
                "pages": 130,
                "language": "Português",
                "format": "PDF",
                "popularity": 91,
            },
            "prosperidade_judeus": {
                "id": "prosperidade_judeus",
                "title": "O Segredo da Prosperidade dos Judeus",
                "author": "Pastor Paulo Coutinho",
                "type": "ebook",
                "price": 10.00,
                "rating": 4.9,
                "reviews": 15670,
                "description": "Descubra como aplicar os segredos milenares da prosperidade judaica para transformar sua vida financeira e alcançar o sucesso verdadeiro. Este livro é um convite para explorar os princípios e valores que têm guiado a prosperidade do povo judeu ao longo dos séculos, com uma abordagem prática e estratégica.",
                "category": "Finanças Cristãs",
                "pages": 180,
                "language": "Português",
                "format": "PDF",
                "popularity": 99,
            },
        }

        self.orders = {}
        self.customer_info = {}

    def search_books(self, query: str) -> List[Dict[str, Any]]:
        """Search books by title, author, or category"""
        query = query.lower()
        results = []

        for book in self.books.values():
            if (
                query in book["title"].lower()
                or query in book["author"].lower()
                or query in book["category"].lower()
                or query in book["description"].lower()
            ):
                results.append(book)

        return results

    def get_popular_books(self, limit: int = 5) -> List[Dict[str, Any]]:
        """Returns the most popular books"""
        sorted_books = sorted(
            self.books.values(), key=lambda x: x["popularity"], reverse=True
        )
        return sorted_books[:limit]

    def get_book_details(self, book_id: str) -> Optional[Dict[str, Any]]:
        """Returns details of a specific book"""
        return self.books.get(book_id)

    def create_order(
        self, book_id: str, customer_email: str, customer_phone: str
    ) -> Dict[str, Any]:
        """Creates an order"""
        book = self.books.get(book_id)
        if not book:
            return None

        order_id = f"ORD{datetime.now().strftime('%Y%m%d%H%M%S')}"
        order = {
            "id": order_id,
            "book_id": book_id,
            "book_title": book["title"],
            "price": book["price"],
            "customer_email": customer_email,
            "customer_phone": customer_phone,
            "order_date": datetime.now(),
            "status": "confirmed",
        }

        self.orders[order_id] = order
        self.customer_info[customer_email] = {
            "email": customer_email,
            "phone": customer_phone,
            "orders": [order_id],
        }

        return order
