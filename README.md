# digital-twin-conveyor-
# Digital Twin Conveyor - FIWARE IoT Learning Project

Projeto de aprendizado voltado para a construção de um Gêmeo Digital de uma Correia Transportadora de Minério utilizando tecnologias de IoT, Indústria 4.0 e FIWARE.

O objetivo é simular sensores industriais, processar eventos em tempo real, armazenar histórico operacional e visualizar indicadores por meio de dashboards.

## Arquitetura

Python Simulator → MQTT (Mosquitto) → Node-RED → Orion Context Broker → QuantumLeap → CrateDB → Grafana

## Funcionalidades

* Simulação de sensores industriais
* Comunicação MQTT
* Processamento de eventos com Node-RED
* Gerenciamento de contexto com FIWARE Orion
* Persistência temporal com QuantumLeap e CrateDB
* Dashboards operacionais no Grafana
* Monitoramento de desempenho e condições operacionais
* Cálculo de indicadores e perdas operacionais

## Variáveis Monitoradas

* Belt Speed (Velocidade da Correia)
* Motor Current (Corrente do Motor)
* Vibration (Vibração)
* Load (Carga)
* Production (Produção)
* Loss Per Hour (Perda Financeira por Hora)
* Operational Status (Status Operacional)

## Objetivos de Aprendizado

* MQTT e IoT
* Arquiteturas orientadas a eventos
* FIWARE e Context Brokers
* Bancos de dados de séries temporais
* Dashboards industriais
* Conceitos de Gêmeos Digitais
* Monitoramento de ativos industriais

## Tecnologias

* Python
* Docker
* Docker Compose
* Eclipse Mosquitto
* Node-RED
* FIWARE Orion Context Broker
* QuantumLeap
* CrateDB
* Grafana

Projeto desenvolvido para fins de estudo, experimentação e aprendizado em IoT Industrial e Digital Twins.

