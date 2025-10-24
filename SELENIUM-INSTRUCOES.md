# 🤖 Preenchimento Automático com Selenium

## 🎯 Solução Implementada

Criei uma solução completa usando **Selenium WebDriver** para preenchimento automático dos campos Bubble. Esta solução é muito mais robusta e confiável para ambientes Bubble.

## 📁 Arquivos Criados

1. **`selenium_auto_fill_improved.py`** - Script principal do Selenium
2. **`requirements.txt`** - Dependências Python
3. **`run_auto_fill.bat`** - Script de execução para Windows
4. **`run_auto_fill.sh`** - Script de execução para Linux/Mac
5. **`SELENIUM-INSTRUCOES.md`** - Este arquivo de instruções

## 🚀 Como Usar

### **Opção 1: Execução Automática (Windows)**

1. **Execute o arquivo `run_auto_fill.bat`**
   - Clique duplo no arquivo
   - O script instalará automaticamente as dependências
   - Executará o preenchimento automático

### **Opção 2: Execução Manual**

1. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Execute o script:**
   ```bash
   python selenium_auto_fill_improved.py
   ```

### **Opção 3: Execução em Linux/Mac**

1. **Torne o script executável:**
   ```bash
   chmod +x run_auto_fill.sh
   ```

2. **Execute:**
   ```bash
   ./run_auto_fill.sh
   ```

## 🔧 Configuração

### **Dados Atuais:**
```python
self.auto_data = {
    'token': '1753104f-5a3f-4e9d-a9f7-ac3d48967111',
    'api_url': 'https://theforge-ia.uazapi.com',
    'instance_id': 'default-instance',
    'attendant_id': 'default-attendant'
}
```

### **Para Alterar os Dados:**
1. Edite o arquivo `selenium_auto_fill_improved.py`
2. Modifique a variável `self.auto_data` (linha ~25)
3. Execute novamente

### **Para Alterar a URL:**
1. Edite o arquivo `selenium_auto_fill_improved.py`
2. Modifique a variável `url` na função `main()` (linha ~200)
3. Execute novamente

## 🎯 Como Funciona

### **1. Configuração do Driver:**
- Baixa automaticamente o ChromeDriver
- Configura opções otimizadas para Bubble
- Evita detecção de automação

### **2. Navegação:**
- Abre o site no Chrome
- Aguarda elementos Bubble carregarem
- Detecta campos de input

### **3. Preenchimento:**
- Encontra campos com placeholder "INSTANCIA"
- Preenche automaticamente com o token
- Dispara eventos para garantir reconhecimento

### **4. Salvamento:**
- Procura botão de salvar
- Clica automaticamente
- Aguarda processamento

## 🔍 Detecção de Campos

O script detecta campos usando múltiplos seletores:

```python
selectors = [
    'input[placeholder="INSTANCIA"]',
    'input[placeholder*="INSTANCIA"]',
    'input[placeholder*="token"]',
    'input[placeholder*="Token"]',
    'input[placeholder*="URL"]',
    'input[placeholder*="url"]',
    'input.bubble-element.Input',
    'input[class*="bubble-element"]',
    'input[type="text"]',
    'input[type="url"]',
    'input:not([type])'
]
```

## 📊 Logs e Debugging

### **Arquivo de Log:**
- `selenium_auto_fill.log` - Log detalhado de execução

### **Mensagens no Console:**
- 🚀 `Iniciando preenchimento automático...`
- 🔍 `Campo encontrado: input[placeholder="INSTANCIA"]`
- ✅ `Campo preenchido com: 1753104f-5a3f-4e9d-a9f7-ac3d48967111`
- ✅ `Preenchimento concluído: X/Y campos preenchidos`

## 🛠️ Requisitos

### **Sistema:**
- Python 3.7+
- Google Chrome instalado
- Conexão com internet

### **Dependências:**
- `selenium==4.15.2`
- `webdriver-manager==4.0.1`

## 🚨 Solução de Problemas

### **Erro: "ChromeDriver not found"**
- O webdriver-manager baixa automaticamente
- Verifique se o Chrome está instalado

### **Erro: "No such element"**
- Aguarde mais tempo para carregar
- Verifique se a URL está correta

### **Erro: "Permission denied"**
- Execute como administrador (Windows)
- Use `sudo` (Linux/Mac)

### **Campos não preenchidos:**
- Verifique o arquivo de log
- Ajuste os seletores se necessário

## 🎯 Vantagens do Selenium

### **✅ Confiabilidade:**
- Funciona com qualquer site
- Não depende de CORS
- Controla o navegador diretamente

### **✅ Flexibilidade:**
- Pode ser executado localmente
- Pode ser executado em servidor
- Pode ser agendado

### **✅ Debugging:**
- Logs detalhados
- Pode pausar para inspeção
- Interface visual

### **✅ Compatibilidade:**
- Funciona com Bubble
- Funciona com qualquer framework
- Funciona em qualquer navegador

## 🔄 Agendamento

### **Windows (Task Scheduler):**
1. Abra o Agendador de Tarefas
2. Crie nova tarefa
3. Configure para executar `run_auto_fill.bat`
4. Defina horário desejado

### **Linux/Mac (Cron):**
```bash
# Executa a cada hora
0 * * * * /caminho/para/run_auto_fill.sh
```

## 📱 Execução Remota

### **Servidor VPS:**
- Execute em servidor Linux
- Use `headless=True` para não abrir interface
- Configure cron para execução automática

### **Docker:**
```dockerfile
FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "selenium_auto_fill_improved.py"]
```

## 🎉 Resultado

Com esta solução, você terá:
- ✅ **Preenchimento automático** confiável
- ✅ **Execução agendada** (opcional)
- ✅ **Logs detalhados** para debugging
- ✅ **Compatibilidade total** com Bubble
- ✅ **Facilidade de uso** com scripts de execução

---

**Nota**: Esta solução com Selenium é muito mais robusta e confiável que as abordagens JavaScript anteriores, especialmente para ambientes Bubble!
