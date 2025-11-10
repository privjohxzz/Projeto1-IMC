# Gerar arquivo README.md com o conteúdo formatado
readme_content = """# 🧮 Projeto IMC (Índice de Massa Corporal)

## 📘 Descrição
A nutricionista **Dra. Clara Souza** precisa de um sistema simples para calcular rapidamente o **IMC (Índice de Massa Corporal)** de seus pacientes.  
O objetivo deste projeto é desenvolver um programa que receba o **peso** e a **altura** de uma pessoa e retorne o valor do **IMC** e sua **classificação** conforme a tabela oficial da **OMS (Organização Mundial da Saúde)**.

---

## ⚙️ Tecnologias Utilizadas
Você pode implementar este projeto em qualquer linguagem de programação, como:
- Python 🐍  
- JavaScript 💻  
- C / C++ ⚙️  
- Java ☕  
- Ou outra linguagem de sua preferência!

---

## 🧩 Requisitos do Projeto

### 1️⃣ Entrada de Dados
O programa deve solicitar ao usuário:
- **Nome do paciente**
- **Peso** em quilogramas (kg)
- **Altura** em metros (m)

---

### 2️⃣ Cálculo do IMC
A fórmula do IMC é:

\\[
IMC = \\frac{Peso (kg)}{Altura (m)^2}
\\]

---

### 3️⃣ Classificação (OMS)

| IMC (kg/m²) | Classificação |
|--------------|---------------|
| Menor que 18.5 | Abaixo do peso |
| 18.5 – 24.9 | Peso normal |
| 25.0 – 29.9 | Sobrepeso |
| 30.0 – 34.9 | Obesidade grau 1 |
| 35.0 – 39.9 | Obesidade grau 2 |
| Maior ou igual a 40.0 | Obesidade grau 3 |

---

### 4️⃣ Saída Formatada
O sistema deve exibir:
- O **nome do paciente**  
- O **IMC** (com duas casas decimais)  
- A **classificação correspondente**

---

## 🧪 Exemplo de Execução

```bash
Digite o nome do paciente: João da Silva
Digite o peso (kg): 85
Digite a altura (m): 1.75

João da Silva tem IMC igual a 27.76, classificado como Sobrepeso.
