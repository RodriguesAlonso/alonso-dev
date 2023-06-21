function executarCodigo() {
    const codigoInput = document.getElementById('codigo');
    const saidaDiv = document.getElementById('saida');
    const codigo = codigoInput.value;

    // Limpa a saída
    saidaDiv.innerHTML = '';

    try {
        // Executa o código Python usando um servidor backend
        // Neste exemplo, usaremos o serviço "pyodide" para executar Python no navegador
        // Certifique-se de incluir a biblioteca Pyodide no seu projeto
        pyodide.runPython(codigo);

        // Captura a saída do código Python e exibe na janela
        const stdout = pyodide.runPython('print(*pyodide._pyodide.sys.stdout)');
        saidaDiv.innerHTML = stdout;
    } catch (e) {
        console.error(e);
        saidaDiv.innerHTML = 'Erro ao executar o código Python.';
    }
}