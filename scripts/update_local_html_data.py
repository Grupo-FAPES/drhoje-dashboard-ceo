import base64
import json
import re

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find const DATA_RAW = "..."
    match = re.search(r'const DATA_RAW = "(.*?)";', content)
    if not match:
        print(f"DATA_RAW not found in {filepath}")
        return
    
    raw_b64 = match.group(1)
    # Decode
    decoded = base64.b64decode(raw_b64).decode('utf-8')
    data = json.loads(decoded)
    
    # Modify data to show only July inclusions
    data["pagina1_visao_executiva"]["kpis"]["inclusoes_junho"] = 30
    data["pagina1_visao_executiva"]["kpis"]["inclusoes_junho_obs"] = "Julho/2026 (até 17/07/2026)"
    data["pagina1_visao_executiva"]["kpis"]["inclusoes_titulo"] = "INCLUSÕES EM JULHO"
    data["pagina1_visao_executiva"]["inclusoes_junho_por_consultor"] = {
        "mes_ref": "Julho/2026 (até 17/07/2026)",
        "itens": [
            {"consultor": "ECONOMIA SEGUROS", "tipo": "EMPRESARIAL", "inclusoes": 10, "pct": 33.3, "valor": 95.0},
            {"consultor": "VENDA DIRETA", "tipo": "ADESÃO", "inclusoes": 8, "pct": 26.7, "valor": 1087.1},
            {"consultor": "CONFIER CORRETORA DE SEGUROS", "tipo": "EMPRESARIAL", "inclusoes": 6, "pct": 20.0, "valor": 114.0},
            {"consultor": "MARSO CORRETORA DE SEGUROS LTDA", "tipo": "EMPRESARIAL", "inclusoes": 3, "pct": 10.0, "valor": 65.4},
            {"consultor": "SAMUEL SOUZA", "tipo": "ADESÃO", "inclusoes": 2, "pct": 6.7, "valor": 112.7},
            {"consultor": "BIANCA SILVA", "tipo": "ADESÃO", "inclusoes": 1, "pct": 3.3, "valor": 22.5}
        ],
        "total": 30,
        "valor_total": 1496.7
    }
    data["pagina1_visao_executiva"]["destaques_periodo"] = [
        {
            "data": "Acompanhamento Mensal",
            "texto": "Inclusões no período de Julho: 30 vidas registradas."
        }
    ]
        
    # Re-encode
    new_json_str = json.dumps(data, ensure_ascii=False)
    new_b64 = base64.b64encode(new_json_str.encode('utf-8')).decode('utf-8')
    
    # Replace in file content
    new_content = content.replace(raw_b64, new_b64)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {filepath} successfully.")

update_file("index.html")
update_file("dashboard_dr_hoje.html")
