from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro/empresa')
def cadastro_empresa():
    return render_template('cadastro/empresa.html')

# Adicione mais rotas de cadastro conforme necessário

@app.route('/movimento/ordem_de_servico')
def ordem_de_servico():
    return render_template('movimento/ordem_de_servico.html')

@app.route('/financeiro/contas_a_pagar')
def contas_a_pagar():
    return render_template('financeiro/contas_a_pagar.html')

# Adicione mais rotas financeiras conforme necessário

@app.route('/diversos/contrato_de_locacao')
def contrato_de_locacao():
    return render_template('diversos/contrato_de_locacao.html')

# Adicione mais rotas diversos conforme necessário

@app.route('/relatorio/relatorio')
def relatorio():
    return render_template('relatorio/relatorio.html')

@app.route('/manutencao/backup')
def backup():
    return render_template('manutencao/backup.html')

# Adicione mais rotas de manutenção conforme necessário

@app.route('/controles/historico')
def historico():
    return render_template('controles/historico.html')

@app.route('/sistema/sobre')
def sobre():
    return render_template('sistema/sobre.html')

@app.route('/sistema/sair')
def sair():
    return render_template('sistema/sair.html')

if __name__ == '__main__':
    app.run(debug=True)
