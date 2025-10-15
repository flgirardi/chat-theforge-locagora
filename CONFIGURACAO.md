# 🔧 Configuração de Dados Automáticos

## 📋 Dados Hardcoded

Os seguintes dados são injetados automaticamente quando o usuário acessa o site:

```javascript
const AUTO_DATA = {
    token: '1753104f-5a3f-4e9d-a9f7-ac3d48967111',
    apiUrl: 'https://theforge-ia.uazapi.com',
    instanceId: 'default-instance',
    attendantId: 'default-attendant'
};
```

## 🛠️ Como Personalizar

### 1. **Alterar o Token**
No arquivo `index.html`, linha 145:
```javascript
token: 'SEU_TOKEN_AQUI',
```

### 2. **Alterar a URL da API**
No arquivo `index.html`, linha 146:
```javascript
apiUrl: 'https://sua-api.com',
```

### 3. **Alterar IDs**
No arquivo `index.html`, linhas 147-148:
```javascript
instanceId: 'seu-instance-id',
attendantId: 'seu-attendant-id'
```

## 🎯 Como Funciona

### **Métodos de Injeção:**

1. **localStorage**: Salva os dados no armazenamento local do iframe
2. **Preenchimento de Campos**: Procura e preenche campos de formulário automaticamente
3. **postMessage**: Envia dados via mensagens entre frames
4. **Eventos**: Dispara eventos de input/change para simular digitação

### **Timing:**
- Aguarda 2 segundos após carregar o iframe
- Tenta novamente após 3 segundos se necessário
- Funciona mesmo com restrições CORS

## 🔍 Debugging

Abra o **Console do Navegador** (F12) para ver:

- ✅ `Dados injetados automaticamente:` - Sucesso na injeção
- ⚠️ `Não foi possível injetar dados automaticamente` - Normal devido ao CORS
- 📨 `Mensagem recebida do Bubble:` - Comunicação com o Bubble

## 📱 Compatibilidade

- ✅ **Desktop**: Funciona perfeitamente
- ✅ **Mobile**: Funciona em dispositivos móveis
- ✅ **CORS**: Funciona mesmo com restrições de segurança
- ✅ **Bubble**: Compatível com aplicações Bubble

## 🚨 Importante

- **Token**: Mantenha o token seguro e atualizado
- **URLs**: Verifique se as URLs da API estão corretas
- **IDs**: Ajuste os IDs conforme sua configuração específica

## 🔄 Atualizações

Para atualizar os dados:
1. Edite o arquivo `index.html`
2. Faça novo deploy no Netlify
3. Os dados serão atualizados automaticamente

---

**Nota**: Se precisar de dados diferentes ou tiver problemas, me avise que posso ajustar o código!
