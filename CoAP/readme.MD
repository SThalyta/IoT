## Servidor CoAP com Python (aiocoap)

Este projeto é um exemplo de servidor CoAP utilizando a biblioteca `aiocoap` em Python. Ele simula dois recursos simples para aplicações IoT:

### Rotas disponíveis

- `/temperatura`:  
  Simula a leitura de um sensor de temperatura.  
  **Método permitido:** `GET`  
  **Retorno:** Um valor de temperatura aleatório entre 20.0 e 30.0°C, arredondado em duas casas decimais.

- `/lampada`:  
  Simula o controle de uma lâmpada.  
  **Métodos permitidos:**  
  - `GET`: Retorna o estado atual da lâmpada (`on` ou `off`)  
  - `PUT`: Altera o estado da lâmpada. Payload deve ser `"on"` ou `"off"`.

---

### Como executar o servidor

1. **Instale as dependências (se ainda não tiver):**
   ```bash
   pip install aiocoap
   ```
2. **Rode o servidor**
  ```bash
   python server.py
   ```
3. **Teste**

    Para simular os clientes, execute os arquivos python disponíveis em outra janela cmd: python nome_do_arquivo.py.

