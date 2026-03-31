import os
import re

directory = r"c:\Users\user\Desktop\THINK-IN\IYRP_2026\WEB IYRP2026"
html_pattern = re.compile(r"<!-- Logos Bottom -->.*?<div class=\"footer-legal-bottom\"", re.DOTALL)

replacement = """<!-- Logos Bottom -->
                <div class="new-footer-logos" style="display: block; width: 100%; max-width: 1200px; margin: 0 auto; padding: 2rem 1rem; box-sizing: border-box;">
                    
                    <style>
                        .footer-logos-container { width: 100%; margin-bottom: 2rem; }
                        .footer-logos-title { font-size: 13px; font-weight: bold; color: #333; margin-bottom: 15px; line-height: 1.4; font-family: sans-serif; text-align: left; }
                        .footer-strip { background-color: #ffffff; width: 100%; display: flex; justify-content: flex-start; align-items: center; padding: 10px 0; box-sizing: border-box; flex-wrap: wrap; gap: 30px; }
                        .footer-strip a { flex: 0 0 auto; display: flex; justify-content: center; align-items: center; }
                        .strip-logo { max-height: 55px; width: auto; object-fit: contain; }
                        .strip-logo-large { max-height: 65px; width: auto; object-fit: contain; } 
                        
                        @media (max-width: 900px) {
                            .footer-strip { justify-content: center; }
                            .footer-logos-title { text-align: center; }
                        }
                        @media (max-width: 600px) {
                            .strip-logo { max-height: 45px; }
                            .strip-logo-large { max-height: 55px; }
                            .footer-strip { gap: 20px; }
                        }
                    </style>

                    <!-- Top section: Comité Organizador -->
                    <div class="footer-logos-container">
                        <div class="footer-logos-title">Comité Organizador / Organizing Committee / Comité D'organisation</div>
                        <div class="footer-strip">
                            <a href="https://iyrp.info" target="_blank" style="display: block;"><img src="estilos/logos/logo_iyrp.png" alt="IYRP" class="strip-logo"></a>
                            <a href="https://www.fao.org" target="_blank" style="display: block;"><img src="estilos/logos/fao_logo_blue_3lines_es.png" alt="FAO" class="strip-logo-large"></a>
                            <a href="https://www.iamz.ciheam.org" target="_blank" style="display: block;"><img src="estilos/logos/ciheam_zaragoza_cmjn_horizontal.png" alt="CIHEAM Zaragoza" class="strip-logo" style="max-height: 50px;"></a>
                            <a href="https://trashumanciaynaturaleza.org" target="_blank" style="display: block;"><img src="estilos/logos/fundacionlogo.png" alt="Fundación Trashumancia y Naturaleza" class="strip-logo"></a>
                            <a href="https://www.comunidad.madrid" target="_blank" style="display: block;"><img src="estilos/logos/comunidad_de_madrid.png" alt="Comunidad de Madrid" class="strip-logo" style="max-height: 48px;"></a>
                        </div>
                    </div>

                    <!-- Middle section: Patrocinado por -->
                    <div class="footer-logos-container">
                        <div class="footer-logos-title">Patrocinado por / Sponsored by / Avec l'appui financier de</div>
                        <div class="footer-strip">
                            <a href="https://www.entretantos.org" target="_blank" style="display: block;"><img src="estilos/logos/entretantos_nueva_grande.png" alt="Entretantos" class="strip-logo"></a>
                            <a href="https://fundacion-biodiversidad.es" target="_blank" style="display: block;"><img src="estilos/logos/vice3mitecofb_banderas_color.png" alt="Ministerio" class="strip-logo"></a>
                            <a href="https://www.ree.es" target="_blank" style="display: block;"><img src="estilos/logos/REDELECTRICA_POS_RGB.png" alt="Red Eléctrica" class="strip-logo"></a>
                            <a href="https://www.landcoalition.org" target="_blank" style="display: block;"><img src="estilos/logos/ilc_logo_standard_black_convertido.png" alt="ILC" class="strip-logo"></a>
                        </div>
                    </div>
                        
                    <!-- Bottom section: Colabora -->
                    <div class="footer-logos-container" style="margin-bottom: 0;">
                        <div class="footer-logos-title">Colabora / Collaborators / Collaborateurs</div>
                        <div class="footer-strip">
                            <a href="https://www.interovic.es" target="_blank" style="display: block;"><img src="estilos/logos/interovic_logo_03.png" alt="Interovic" class="strip-logo"></a>
                            <a href="https://rfeagas.es" target="_blank" style="display: block;"><img src="estilos/logos/logo_rfeagas_.png" alt="RFEAGAS" class="strip-logo"></a>
                            <a href="https://aranjuez.es" target="_blank" style="display: block;"><img src="estilos/logos/Ayto%20Aranjuez%20firma_web.png" alt="Aranjuez" class="strip-logo"></a>
                        </div>
                    </div>
                </div>

                <div class="footer-legal-bottom\"""" 

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = html_pattern.sub(replacement, content)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {filename}")
