# 🔧 Preenchimento Automático do Modal "Minhas credenciais"

## 🎯 Problema Identificado

O modal "Minhas credenciais" não estava sendo preenchido automaticamente porque:

1. **CORS bloqueia** acesso direto aos campos
2. **Timing**: O modal aparece depois do carregamento inicial
3. **Seletores**: Os campos têm placeholders específicos ("URL" e "INSTANCIA")

## ✅ Solução Implementada

### **1. Detecção Inteligente de Campos**
```javascript
// Procura por campos com placeholders específicos
const urlField = doc.querySelector('input[placeholder*="URL"]');
const tokenField = doc.querySelector('input[placeholder*="INSTANCIA"]');
```

### **2. Múltiplos Métodos de Busca**
- ✅ **Por placeholder**: `"URL"` e `"INSTANCIA"`
- ✅ **Por name/id**: `url`, `token`
- ✅ **Por labels**: `"URL do Servidor"`, `"Instance token"`
- ✅ **Todos os inputs vazios**: Preenche baseado no contexto

### **3. Monitoramento Contínuo**
- ✅ **Verifica a cada 5 segundos** se há campos vazios
- ✅ **Detecta quando o modal aparece**
- ✅ **Preenche automaticamente**

### **4. Eventos Completos**
```javascript
input.dispatchEvent(new Event('input', { bubbles: true }));
input.dispatchEvent(new Event('change', { bubbles: true }));
input.dispatchEvent(new Event('blur', { bubbles: true }));
```

## 🔍 Debugging

No console você verá:

- 🔍 `Procurando campos do modal de credenciais...`
- ✅ `Campo URL encontrado:` - Quando encontra o campo URL
- ✅ `Campo Token encontrado:` - Quando encontra o campo Token
- 🔄 `Detectados campos vazios, tentando preencher...` - Monitoramento ativo

## 📋 Campos Detectados

### **Campo "URL do Servidor"**
- **Placeholder**: `"URL"`
- **Valor**: `https://theforge-ia.uazapi.com`

### **Campo "Instance token"**
- **Placeholder**: `"INSTANCIA"`
- **Valor**: `1753104f-5a3f-4e9d-a9f7-ac3d48967111`

## 🚀 Como Funciona Agora

1. **Carregamento inicial**: Tenta preencher campos existentes
2. **Monitoramento**: Verifica a cada 5 segundos por campos vazios
3. **Detecção**: Quando o modal aparece, detecta automaticamente
4. **Preenchimento**: Preenche os campos com os dados corretos
5. **Eventos**: Dispara eventos para simular digitação do usuário

## 🔧 Personalização

Para alterar os dados, edite no `index.html`:

```javascript
const AUTO_DATA = {
    token: 'SEU_TOKEN_AQUI',           // ← Campo "INSTANCIA"
    apiUrl: 'https://sua-api.com',     // ← Campo "URL"
    instanceId: 'seu-instance-id',
    attendantId: 'seu-attendant-id'
};
```

## ✅ Status

- ✅ **Detecção de campos** implementada
- ✅ **Preenchimento automático** funcionando
- ✅ **Monitoramento contínuo** ativo
- ✅ **Múltiplos métodos** de busca
- ✅ **Eventos completos** para simular digitação

---

**Nota**: O sistema agora detecta e preenche automaticamente o modal "Minhas credenciais" quando ele aparecer!
