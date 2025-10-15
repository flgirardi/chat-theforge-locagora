# UAZapigo Multi-Atendimento - Proxy Site

Este projeto cria um proxy para o site UAZapigo Multi-Atendimento hospedado no Bubble, permitindo que você tenha seu próprio domínio no Netlify enquanto mantém toda a funcionalidade do site original.

## 🚀 Como fazer o deploy no Netlify

### Opção 1: Deploy via GitHub (Recomendado)

1. **Crie um repositório no GitHub:**
   - Faça upload dos arquivos deste projeto para um novo repositório
   - Ou conecte este projeto local a um repositório GitHub

2. **Conecte ao Netlify:**
   - Acesse [netlify.com](https://netlify.com)
   - Clique em "New site from Git"
   - Conecte sua conta GitHub
   - Selecione o repositório criado
   - O Netlify detectará automaticamente as configurações do `netlify.toml`

3. **Deploy automático:**
   - O site será deployado automaticamente
   - Você receberá um link do tipo `https://seu-site.netlify.app`

### Opção 2: Deploy manual via drag & drop

1. **Prepare os arquivos:**
   - Certifique-se de que todos os arquivos estão na pasta raiz
   - Comprima a pasta em um arquivo ZIP

2. **Deploy no Netlify:**
   - Acesse [netlify.com](https://netlify.com)
   - Arraste e solte o arquivo ZIP na área de deploy
   - Aguarde o processo de deploy

### Opção 3: Deploy via Netlify CLI

```bash
# Instale o Netlify CLI
npm install -g netlify-cli

# Faça login
netlify login

# Deploy
netlify deploy --prod --dir .
```

## 🔧 Configurações

### Personalização do domínio

Após o deploy, você pode:

1. **Usar o domínio padrão do Netlify:**
   - `https://seu-site.netlify.app`

2. **Configurar um domínio personalizado:**
   - Vá em Site settings > Domain management
   - Adicione seu domínio personalizado
   - Configure os DNS conforme instruções do Netlify

### Configurações de segurança

O arquivo `netlify.toml` já inclui:
- Headers de segurança apropriados
- Configurações de iframe
- Redirecionamentos para SPA

## 📱 Funcionalidades

- ✅ **URL fixa:** A URL do seu domínio não muda no navegador
- ✅ **Responsivo:** Funciona em desktop e mobile
- ✅ **Loading state:** Mostra carregamento enquanto o site carrega
- ✅ **Error handling:** Trata erros de carregamento
- ✅ **Retry:** Botão para tentar novamente em caso de erro
- ✅ **Segurança:** Headers de segurança configurados

## 🛠️ Manutenção

### Atualizar o site original

Se o site do Bubble for atualizado, suas mudanças aparecerão automaticamente no seu proxy, pois ele carrega o conteúdo em tempo real.

### Monitoramento

- Use o dashboard do Netlify para monitorar:
  - Visitas ao site
  - Performance
  - Erros de deploy
  - Logs de função (se usar)

## 📞 Suporte

Se precisar de ajuda com:
- Deploy no Netlify
- Configuração de domínio personalizado
- Problemas de carregamento
- Personalizações adicionais

Entre em contato para suporte técnico.

---

**Nota:** Este projeto funciona como um proxy transparente para o site original do Bubble, mantendo toda a funcionalidade enquanto permite que você tenha seu próprio domínio.
