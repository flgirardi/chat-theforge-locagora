# 🎯 Configuração para Ambiente Bubble

## 🚨 Problema Identificado

Quando o site é executado dentro de um ambiente Bubble, as restrições de CORS e o contexto são diferentes, o que pode impedir o preenchimento automático dos campos.

## 🔧 Soluções Implementadas

### 1. **Múltiplos Métodos de Injeção**

O sistema agora usa **5 métodos diferentes** para garantir o preenchimento:

1. **URL Parameters** (mais confiável)
2. **postMessage** (comunicação entre frames)
3. **Acesso direto ao iframe**
4. **window.parent** (comunicação com Bubble)
5. **localStorage/sessionStorage** (persistência de dados)

### 2. **Sistema de Retry Agressivo**

- **20 tentativas** de preenchimento automático
- **Intervalo de 2 segundos** entre tentativas
- **Monitoramento contínuo** a cada 3 segundos
- **Detecção de eventos** (click, focus, etc.)

### 3. **Detecção de Ambiente Bubble**

O sistema detecta automaticamente se está rodando em um ambiente Bubble e:
- Ajusta a estratégia de injeção
- Monitora elementos Bubble específicos
- Usa MutationObserver para detectar novos elementos

### 4. **Persistência de Dados**

Os dados são salvos em:
- `localStorage` da página principal
- `sessionStorage` da página principal
- `localStorage` do iframe (quando possível)

## 🎯 Como Funciona Agora

### **Carregamento Inicial:**
1. Página carrega com dados na URL
2. Sistema detecta ambiente Bubble
3. Injeta dados via múltiplos métodos
4. Inicia retry agressivo

### **Monitoramento Contínuo:**
1. Verifica campos vazios a cada 3 segundos
2. Tenta preencher quando detecta campos vazios
3. Responde a eventos do usuário (click, focus)
4. Monitora elementos Bubble que aparecem

### **Comunicação com Bubble:**
1. Envia dados via `postMessage`
2. Comunica com `window.parent`
3. Salva dados no `localStorage`
4. Escuta mensagens do Bubble

## 🔍 Debugging

Para verificar se está funcionando, abra o **Console do Navegador** (F12) e procure por:

### **Mensagens de Sucesso:**
- 🚀 `Tentando injetar dados automaticamente...`
- 🎯 `Ambiente Bubble detectado!`
- ✅ `Dados salvos no localStorage/sessionStorage`
- ✅ `Campo INSTANCIA preenchido com sucesso!`

### **Mensagens de Retry:**
- 🔄 `Tentativa X/20 de preenchimento automático...`
- 🔍 `Acesso direto ao iframe conseguido!`
- 📤 `Enviando dados para window.parent...`

### **Mensagens de Detecção:**
- 🎯 `Elemento Bubble detectado, injetando dados...`
- 👆 `Usuário clicou, tentando injetar dados...`
- 🎯 `Página ganhou foco, tentando injetar dados...`

## 🛠️ Configuração

### **Dados Atuais:**
```javascript
const AUTO_DATA = {
    token: '1753104f-5a3f-4e9d-a9f7-ac3d48967111',
    apiUrl: 'https://theforge-ia.uazapi.com',
    instanceId: 'default-instance',
    attendantId: 'default-attendant'
};
```

### **Para Alterar os Dados:**
1. Edite o arquivo `index.html`
2. Modifique a constante `AUTO_DATA` (linha ~145)
3. Faça novo deploy

## 🚨 Solução de Problemas

### **Se ainda não estiver funcionando:**

1. **Verifique o Console:**
   - Abra F12 → Console
   - Procure por mensagens de erro
   - Verifique se os dados estão sendo enviados

2. **Teste os Métodos:**
   - Verifique se os dados estão na URL
   - Confirme se o localStorage tem os dados
   - Teste se o postMessage está funcionando

3. **Ambiente Bubble:**
   - Confirme se está rodando em ambiente Bubble
   - Verifique se os elementos Bubble estão sendo detectados
   - Teste se o MutationObserver está funcionando

## 📱 Compatibilidade

- ✅ **Ambiente Bubble**: Otimizado para Bubble
- ✅ **Desktop**: Funciona perfeitamente
- ✅ **Mobile**: Funciona em dispositivos móveis
- ✅ **CORS**: Funciona mesmo com restrições
- ✅ **Retry**: Sistema robusto de tentativas

## 🎯 Status Atual

- ✅ **5 métodos de injeção** implementados
- ✅ **Sistema de retry agressivo** ativo
- ✅ **Detecção de ambiente Bubble** funcionando
- ✅ **Monitoramento contínuo** ativo
- ✅ **Persistência de dados** implementada

---

**Nota**: O sistema agora é muito mais robusto para ambientes Bubble e deve funcionar mesmo com restrições de CORS e contextos específicos do Bubble.
