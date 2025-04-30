# DOS-blocker

Este projeto tem como objetivo detectar e bloquear ataques de negação de serviço (DoS) com base na taxa de pacotes recebidos por IP. Ele monitora o tráfego de rede e bloqueia automaticamente os endereços IP que excedem um limite definido de requisições por segundo.

1.Monitora o tráfego de rede em tempo real.
2.Conta os pacotes recebidos por IP.
3.Bloqueia IPs que ultrapassarem o limite definido (THRESHOLD).
4.Gera regras de bloqueio no firewall (iptables) automaticamente.

O projeto inclui um script para ser testado.

Utilidade:
Este script fornece um mecanismo simples e eficaz para detectar comportamentos suspeitos e proteger a rede de maneira automática.

Requisitos:
1.Python 3
2.Scapy
3.Permissões de superusuário (root)
