#!/usr/bin/env python3
"""
Script Selenium melhorado para preenchimento automático de campos Bubble
UAZapigo Multi-Atendimento - Preenchimento Automático com WebDriver Manager
"""

import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('selenium_auto_fill.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class BubbleAutoFillerImproved:
    def __init__(self, headless=False):
        """
        Inicializa o driver do Selenium com configurações otimizadas para Bubble
        """
        self.driver = None
        self.wait = None
        self.headless = headless
        self.auto_data = {
            'token': '1753104f-5a3f-4e9d-a9f7-ac3d48967111',
            'api_url': 'https://theforge-ia.uazapi.com',
            'instance_id': 'default-instance',
            'attendant_id': 'default-attendant'
        }
        
    def setup_driver(self):
        """
        Configura o driver do Chrome com webdriver-manager
        """
        chrome_options = Options()
        
        if self.headless:
            chrome_options.add_argument('--headless')
        
        # Configurações para melhor compatibilidade com Bubble
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
        
        # Configurações para evitar detecção de automação
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        try:
            # Usa webdriver-manager para baixar automaticamente o ChromeDriver
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            self.wait = WebDriverWait(self.driver, 20)
            logger.info("✅ Driver do Chrome configurado com sucesso")
            return True
        except Exception as e:
            logger.error(f"❌ Erro ao configurar driver: {e}")
            return False
    
    def navigate_to_site(self, url):
        """
        Navega para o site e aguarda o carregamento
        """
        try:
            logger.info(f"🌐 Navegando para: {url}")
            self.driver.get(url)
            
            # Aguarda o carregamento inicial
            time.sleep(5)
            
            # Aguarda elementos específicos do Bubble carregarem
            self.wait_for_bubble_elements()
            
            logger.info("✅ Site carregado com sucesso")
            return True
            
        except Exception as e:
            logger.error(f"❌ Erro ao navegar para o site: {e}")
            return False
    
    def wait_for_bubble_elements(self):
        """
        Aguarda elementos específicos do Bubble carregarem
        """
        try:
            # Aguarda elementos bubble-element aparecerem
            self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[class*="bubble-element"]'))
            )
            logger.info("✅ Elementos Bubble detectados")
            
            # Aguarda um pouco mais para garantir que tudo carregou
            time.sleep(3)
            
        except TimeoutException:
            logger.warning("⚠️ Timeout aguardando elementos Bubble")
    
    def find_input_fields(self):
        """
        Encontra todos os campos de input que precisam ser preenchidos
        """
        input_fields = []
        
        # Seletores para encontrar campos de input
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
        
        for selector in selectors:
            try:
                elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                for element in elements:
                    if element.is_displayed() and element.is_enabled():
                        input_fields.append(element)
                        logger.info(f"🔍 Campo encontrado: {selector}")
            except Exception as e:
                logger.debug(f"Erro ao buscar seletor {selector}: {e}")
        
        # Remove duplicatas
        unique_fields = []
        seen_elements = set()
        for field in input_fields:
            element_id = id(field)
            if element_id not in seen_elements:
                unique_fields.append(field)
                seen_elements.add(element_id)
        
        logger.info(f"✅ Total de campos únicos encontrados: {len(unique_fields)}")
        return unique_fields
    
    def fill_field(self, field, value):
        """
        Preenche um campo específico com o valor fornecido
        """
        try:
            # Scroll para o elemento
            self.driver.execute_script("arguments[0].scrollIntoView(true);", field)
            time.sleep(0.5)
            
            # Limpa o campo
            field.clear()
            time.sleep(0.2)
            
            # Preenche o campo
            field.send_keys(value)
            time.sleep(0.2)
            
            # Dispara eventos para garantir que o Bubble reconheça
            self.driver.execute_script("""
                arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
                arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
                arguments[0].dispatchEvent(new Event('blur', { bubbles: true }));
            """, field)
            
            logger.info(f"✅ Campo preenchido com: {value}")
            return True
            
        except Exception as e:
            logger.error(f"❌ Erro ao preencher campo: {e}")
            return False
    
    def auto_fill_fields(self):
        """
        Preenche automaticamente todos os campos encontrados
        """
        logger.info("🚀 Iniciando preenchimento automático...")
        
        # Encontra todos os campos
        fields = self.find_input_fields()
        
        if not fields:
            logger.warning("⚠️ Nenhum campo encontrado para preenchimento")
            return False
        
        success_count = 0
        
        for field in fields:
            try:
                # Obtém informações do campo
                placeholder = field.get_attribute('placeholder') or ''
                field_type = field.get_attribute('type') or 'text'
                
                logger.info(f"🔍 Processando campo: placeholder='{placeholder}', type='{field_type}'")
                
                # Determina qual valor usar baseado no placeholder
                value_to_fill = None
                
                if 'INSTANCIA' in placeholder.upper() or 'token' in placeholder.lower():
                    value_to_fill = self.auto_data['token']
                elif 'URL' in placeholder.upper() or 'url' in placeholder.lower():
                    value_to_fill = self.auto_data['api_url']
                elif 'instance' in placeholder.lower():
                    value_to_fill = self.auto_data['instance_id']
                elif 'attendant' in placeholder.lower():
                    value_to_fill = self.auto_data['attendant_id']
                else:
                    # Se não conseguir determinar, tenta com o token
                    value_to_fill = self.auto_data['token']
                
                if value_to_fill:
                    if self.fill_field(field, value_to_fill):
                        success_count += 1
                        time.sleep(0.5)  # Pausa entre campos
                
            except Exception as e:
                logger.error(f"❌ Erro ao processar campo: {e}")
        
        logger.info(f"✅ Preenchimento concluído: {success_count}/{len(fields)} campos preenchidos")
        return success_count > 0
    
    def save_credentials(self):
        """
        Tenta salvar as credenciais clicando no botão de salvar
        """
        try:
            # Procura por botões de salvar
            save_selectors = [
                'button:contains("Salvar")',
                'button:contains("Save")',
                '[class*="save"]',
                '[id*="save"]',
                'button[type="submit"]'
            ]
            
            for selector in save_selectors:
                try:
                    save_button = self.driver.find_element(By.CSS_SELECTOR, selector)
                    if save_button.is_displayed() and save_button.is_enabled():
                        logger.info("🔍 Botão de salvar encontrado")
                        
                        # Scroll para o botão
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", save_button)
                        time.sleep(0.5)
                        
                        # Clica no botão
                        save_button.click()
                        logger.info("✅ Botão de salvar clicado")
                        
                        # Aguarda um pouco para processar
                        time.sleep(2)
                        return True
                        
                except NoSuchElementException:
                    continue
                except Exception as e:
                    logger.error(f"❌ Erro ao clicar no botão de salvar: {e}")
            
            logger.info("ℹ️ Nenhum botão de salvar encontrado")
            return False
            
        except Exception as e:
            logger.error(f"❌ Erro ao tentar salvar credenciais: {e}")
            return False
    
    def run_auto_fill(self, url):
        """
        Executa o processo completo de preenchimento automático
        """
        try:
            # Configura o driver
            if not self.setup_driver():
                return False
            
            # Navega para o site
            if not self.navigate_to_site(url):
                return False
            
            # Aguarda um pouco para garantir que tudo carregou
            time.sleep(3)
            
            # Preenche os campos
            if not self.auto_fill_fields():
                logger.warning("⚠️ Falha no preenchimento automático")
                return False
            
            # Tenta salvar as credenciais
            self.save_credentials()
            
            # Aguarda um pouco para ver o resultado
            time.sleep(3)
            
            logger.info("🎉 Processo de preenchimento automático concluído com sucesso!")
            return True
            
        except Exception as e:
            logger.error(f"❌ Erro durante o processo: {e}")
            return False
        
        finally:
            if self.driver:
                self.driver.quit()
    
    def close(self):
        """
        Fecha o driver
        """
        if self.driver:
            self.driver.quit()
            logger.info("🔒 Driver fechado")

def main():
    """
    Função principal para executar o preenchimento automático
    """
    # URL do site (ajuste conforme necessário)
    url = "https://uazapigo-multiatendimento.bubbleapps.io/"
    
    # Cria instância do auto-filler
    auto_filler = BubbleAutoFillerImproved(headless=False)  # headless=True para executar sem interface
    
    try:
        # Executa o preenchimento automático
        success = auto_filler.run_auto_fill(url)
        
        if success:
            print("✅ Preenchimento automático concluído com sucesso!")
        else:
            print("❌ Falha no preenchimento automático")
            
    except KeyboardInterrupt:
        print("⏹️ Processo interrompido pelo usuário")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
    finally:
        auto_filler.close()

if __name__ == "__main__":
    main()
