<h1 style="text-align: center;">Cadastro manoel bonifacio</h1>

<div style="display: flex; flex-direction: column; align-items: center;">
    <input id="nome" style="width: 33%;" placeholder="Digite seu nome...">
    <br>
    <input id="telefone" style="width: 33%;" placeholder="Digite seu telefone...">
    <br>
    <input id="serie" style="width: 33%;" placeholder="Digite sua serie...">
    <br>
    <input id="dt_nasc" style="width: 33%;" placeholder="Digite sua data de nascimento...">
    <br>
    <button onclick="gerarObj()" style="width: 33%;">Salvar registro</button>
</div>

<script>
    function gerarObj (){
        const nome = document.getElementById('nome').value;
        const telefone = document.getElementById('telefone').value; 
        const serie = document.getElementById('serie').value;
        const dt_nasc = document.getElementById('dt_nasc').value;

        const registro = {
            nome: nome,
            telefone: telefone,
            serie: serie,
            dt_nasc: dt_nasc
        };
        console.log(registro)
    }

</script>