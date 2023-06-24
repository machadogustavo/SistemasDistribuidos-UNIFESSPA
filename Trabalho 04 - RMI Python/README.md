
# Sistemas Distribuidos - UNIFESSPA

### Discentes

- [Gabriel Morandi Mello](https://github.com/gabrielmorandi)
- [Gustavo Paixão Machado](https://github.com/machadogustavo)

## Trabalho – RMI Python

![Interface RMI](./Interface.png)

![](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white) 

*Aplicação de transferência de arquivos em uma arquitetura cliente-servidor.*

```
Utilizar a middleware Java RMI (Remote Invocation Method) ou Pyro 4/5
(Python Remote Objects) para prover a comunicação entre os clientes e o
servidor da aplicação.
```

### Métodos disponíveis no Servidor

- **Fazer upload** de arquivos para serem compartilhados;
- **Consultar** informações sobre os arquivos disponíveis;
- **Fazer download** de arquivos disponíveis;
- **Registrar interesse** em arquivos não disponíveis no momento da consulta.

*Para isso o cliente deve informar o arquivo desejado, sua referência de objeto
remoto e por quanto tempo será válido esse registro. Servidor armazena
esses interesses. Cada vez que um novo arquivo estiver disponível, o
servidor checa a lista de interesses e envia notificações aos clientes
interessados na ocorrência do evento em questão. Esse envio de notificação
ocorrerá via chamada de métodos (isto é, o servidor invocará um método do
cliente para enviar a notificação).*

- **Cancelar registro de interesse.**

### Método disponível no Cliente:

- **Notificar evento: cliente receberá notificações assíncronas de eventos
(arquivos) que sejam do seu interesse.**

### Observações:

- Não é necessário tratar tolerância a falhas do servidor;
- Não é necessário tratar de segurança;
- Desenvolva uma interface amigável;
- Documentar todo o código;
- Equipe: até 3(três) alunos.

[![Google Drive](https://img.shields.io/badge/Google%20Drive-4285F4.svg?style=for-the-badge&logo=Google-Drive&logoColor=white)](https://drive.google.com/drive/folders/16jgU4M0sE4k6m3S-ryhlOr4uTK27exjk?usp=sharing)

## Documentação
