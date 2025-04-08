## Servidor CoAP com Python (aiocoap)

Este projeto é um exemplo de servidor CoAP utilizando a biblioteca `aiocoap` em Python. Ele simula dois recursos simples para aplicações IoT:

### Rotas disponíveis

- `/temperatura`:  
  Simula a leitura de um sensor de temperatura.  
  **Métodos permitidos:** 
  - `GET`: retorna um valor de temperatura aleatório entre 20.0 e 30.0°C, arredondado em duas casas decimais.
  - `GET com observer`: retorna um valor de temperatura aleatório entre 20.0 e 30.0°C, arredondado em duas casas decimais, mas, nesse caso, com inclusão do método observer do CoAP.

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
   python server_1.py
   ```
3. **Teste**

    Para simular os clientes, execute os arquivos python disponíveis em outra janela cmd: python nome_do_arquivo.py.

    O arquivo c_get_observe.py faz um GET para a rota temperatura com o método observe, que funciona como o subscriber do protocolo MQTT. Você faz um GET para buscar a temperatura, recebe o valor e continua observando as mudanças de temperatura dentro do servidor. Isso é útil em aplicações que dependem de uma mudança do estado para acionar algum processo ou funcionalidade.

    O arquivo c_get_temp.py faz uma requisição GET comum, busca a temperatura e encerra a conexão.

    c_get_lamp.py faz também uma requisição GET simples para buscar o estado atual da lâmpada.

    c_put_lamp.py faz uma atualização no estado da lâmpada, é o único cliente que precisa de uma linha de comando "mais elaborada", mas para rodar basta digitar no cmd: python c_put_lamp.py --payload "estado da lâmpada" ("on"/"off")

