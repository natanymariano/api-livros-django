from ninja import Router, Query
from .schemas import LivrosSchema, AvaliacaoSchema, FiltrosSortear
from .models import Livros, Categorias 

livros_router =  Router()

@livros_router.post('/')
def create_livro(request, livro_schema: LivrosSchema):
    nome = livro_schema.dict() ['nome']
    streaming = livro_schema.dict() ['streaming']
    categorias = livro_schema.dict() ['categorias']
    if streaming not in ['F', 'AK']:
        return 400, { 'status': 'Erro: Streaming deve ser F ou AK'}
    livro = Livros (
        nome = nome,
        streaming = streaming
    )
    livro.save()

    for categoria in categorias:
        categoria_temp = Categorias.objects.get(id=categoria)
        livro.categorias.add(categoria_temp)


    return {'status': 'ok'}

@livros_router.put('/{livro_id}')
def avaliar_livro(request, livro_id: int, avaliacao_schema: AvaliacaoSchema):
    avaliacao = avaliacao_schema.dict()['avaliacao']
    comentarios = avaliacao_schema.dict()['comentarios']
    try:
        livro = Livros.objects.get(id=livro_id)
        livro.comentarios = comentarios
        livro.avaliacao = avaliacao
        livro.save()

        return 200, {'status': 'Avaliação realizada com sucesso'}
    except:
        return 500, {'status': 'Erro interno do servidor'}

@livros_router.delete('/{livro_id}')
def deletar_livro(request, livro_id:int):
    livro = Livros.objects.get(id=livro_id)
    livro.delete()
    return livro_id

@livros_router.get('/sortear/')
def sortear_livro(request, filtros: Query[FiltrosSortear]):
    nota_minima = filtros.dict()['nota_minima']
    categoria = filtros.dict()['categorias']
    reler = filtros.dict()['reler']

    livros = Livros.objects.all()
    if not reler:
        livros = livros.filter(nota=None)
        
    if nota_minima:
        livros = livros.filter(nota__gte=nota_minima)
    if categoria:
        livros = livros.filter(categorias__id=categoria)

        livro =livros.order_by('?').first
        print(livros)
    return {'ok': 'ok'}
