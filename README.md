# Dental Solutions of Winter Haven · proposta de site novo

Site de seis páginas para substituir o atual (dentalsolutionsofwh.com), feito para a apresentação ao cliente.
Abra `index.html` em qualquer navegador ou sirva a pasta com um servidor estático.

## A ideia: a cadeia de lagos

Winter Haven é a "Chain of Lakes City": mais de vinte lagos ligados por canais. O consultório fica na Cypress Gardens Boulevard, entre o Lake Eloise e o Lake Winterset. O site inteiro é feito de **um só motivo: o contorno real do Lake Eloise**, tirado do OpenStreetMap.

- **O hero** é o lago em tamanho gigante, cortado pela tela, com uma foto real do Lake Eloise dentro. Um segundo lago, verde-cipreste, aparece atrás: dois lagos, dois dentistas, uma cadeia.
- **Toda foto** do site é recortada na forma do lago. **Todo botão** é o lago deitado. **Toda bolinha de lista** é o lago em miniatura. O rodapé é uma cadeia de nove lagos.
- **A coisa viva:** "How far is your lake?", na faixa verde-petróleo da home. O mapa é desenhado com os contornos reais de 44 lagos da cidade; o visitante escolhe o lago perto do qual mora (no menu ou tocando no mapa) e vê a distância e os minutos aproximados até o consultório.
- **Dois dentistas, um plano** é a manchete, porque é o que o consultório tem que nenhum vizinho tem: um prostodontista (especialista em coroas, próteses, implantes e reconstruções) e um clínico geral no mesmo corredor.
- **Cores do lugar:** papel quente, verde-petróleo do lago, verde-cipreste, um laranja cítrico só nas ações principais. Tipografia: Fraunces (títulos) e Hanken Grotesk (texto), via Google Fonts.

## Páginas

Início (`index.html`), Serviços (`services.html`), Apneia do sono (`sleep-apnea.html`), Doutores (`doctors.html`), Opiniões (`reviews.html`), Contato (`contact.html`). Menu fixo no topo, menu de celular, link ativo marcado.

- **Idiomas:** botão Español / English no topo traduz todas as páginas e fica salvo entre elas. Espanhol em "usted". Alemão aparece só como aviso ("Wir sprechen Deutsch"), porque o Dr. Polo fala alemão.
- **"Aberto agora"** calculado no fuso da Flórida: segunda a quinta, 8h às 17h; sexta com hora marcada.
- **Contato:** formulário-cupom que abre o e-mail com a mensagem pronta (sem backend ainda), mapa estático do OpenStreetMap com o pino no consultório, perguntas frequentes em fichas empilhadas, formas de pagamento.
- **Geração:** as páginas são geradas por `python3 build.py` a partir de um só cabeçalho e rodapé. Edite `build.py` e rode de novo; ou edite os `.html` direto (nesse caso não rode o build).

## O que é amostra e precisa ser confirmado pelo cliente

- **Telefone.** Dois números circulam: (863) 324‑7121 (ADA, Yelp, Healthgrades, usado no site) e (863) 877‑1891 (site atual deles). Confirmar qual é o atual.
- **E-mail.** `maria@dentalsolutionsofwh.com` é o que aparece no diretório verificado pelo próprio consultório. Idealmente trocar por um endereço geral (`hello@` ou `info@`).
- **Horário.** Segunda a quinta 8–17 e sexta com hora marcada vêm de um diretório; o site atual não diz.
- **Terceira dentista.** Healthgrades e WebMD listam a Dra. Nirali Merchant e o Dr. Robert Atkins no endereço; o site atual só fala de Polo e Cruz. Se houver uma terceira pessoa, entra em `doctors.html`.
- **Biografias.** A do Dr. Polo (cum laude 2003, Universidad Francisco Marroquín; prostodontia; inglês, espanhol e alemão) vem do site atual e da ADA. A do Dr. Cruz (cofundador, clínico geral, implantes, espanhol) vem do site atual e de avaliações. O M.S. do Dr. Polo aparece nas credenciais do site atual, mas a instituição não; não foi inventada.
- **Nota no Google.** "4,9 estrelas, mais de 260 avaliações" vem de diretórios de 2024–2025. Conferir o número atual antes de publicar.
- **Depoimentos.** Quatro avaliações públicas (Carol S., Amity K., um paciente anônimo de 2019 e Judee C.), encurtadas. Trocar pelas que o consultório preferir.
- **Convênios.** "A maioria dos planos PPO", CareCredit, cartões e "sem Medicaid/Medicare" vêm de diretórios. Conferir a lista real.
- **Apneia.** Os quatro passos (estudo do sono, impressões, ajuste, revisões) são o fluxo padrão de um aparelho de avanço mandibular; confirmar com o Dr. Polo.
- **Primeira visita.** "Cerca de uma hora", "os dois doutores podem ver o mesmo caso" e "plano com custos por escrito" são promessas razoáveis, mas são do site novo, não do atual.
- **Distâncias** no mapa dos lagos são em linha reta a partir do centro do lago, com minutos estimados; estão marcadas como aproximadas.
- **Fotos dos doutores e do consultório:** não há. Os lugares de retrato em `doctors.html` mostram imagens de arquivo da cidade com a legenda "retrato a entregar pelo consultório".
- Tradução para o espanhol feita por mim; vale uma revisão final por falante nativo.

## Ideias para apresentar ao cliente (além do que já está na página)

1. **Agendamento online de verdade** no lugar do `mailto:` (NexHealth, Zocdoc, ou o sistema que o consultório já usa). O botão "Book a visit" já está no lugar.
2. **Formulário de novo paciente** em inglês e espanhol, preenchido antes da visita, com assinatura digital. O site atual já oferece formulários para baixar; dá para fazer online.
3. **Fotos profissionais** dos dois doutores, da equipe e do consultório. É o maior ganho de confiança possível; as imagens de arquivo da cidade continuam como identidade ao lado delas.
4. **Avaliações reais do Google** puxadas automaticamente para a página de opiniões, com a nota atualizada.
5. **Página de apneia do sono como porta de entrada**: é um serviço raro em consultórios de dentista e rende buscas próprias ("sleep apnea dentist Winter Haven"). A página já existe; falta cadastrar no Google Search Console e no Google Business.
6. **Marcação `Dentist` (schema.org)** já está em todas as páginas; falta o Google Business Profile atualizado com o link novo.
7. **WhatsApp / SMS** como canal de contato, muito usado pela comunidade latina de Polk County.
8. **Vídeo curto do Dr. Polo** (30 s, em inglês e espanhol) explicando o aparelho de apneia, na própria página.
9. **Promoção de primeira visita** (exame + raio‑X com preço fechado), se o consultório fizer isso, cabe como uma linha em "Your first visit".
10. **E-mail profissional geral** (`hello@dentalsolutionsofwh.com`) no lugar do endereço pessoal.
11. **Acessibilidade:** foco visível, contraste alto, texto real em vez de imagens, animações respeitam "reduzir movimento". Manter em qualquer CMS escolhido.

## Imagens usadas e créditos

Nenhuma imagem é apresentada como se fosse do consultório. Os créditos aparecem no rodapé de todas as páginas e em `assets/credits.json` (com links de origem).

| Arquivo | Título | Autor / fonte | Licença |
| --- | --- | --- | --- |
| assets/winter-haven-legoland-florida-island-in-the.jpg | View of Lake Eloise from Island in the Sky, Legoland Florida | Jared from Clermont, via Wikimedia Commons | CC BY 2.0 |
| assets/sunset-lake-howard-winter-haven-fl.jpg | Sunset Lake Howard, Winter Haven, FL | rose3694, via Flickr | CC BY 2.0 |
| assets/hartman-litho-sales-co-ig4-e-8595.jpg | Gardenia Lane in Idylwild Gardens, Winter Haven (postal, anos 40–50) | Hartman Litho Sales Co., via Wikimedia Commons | Domínio público |
| assets/jacaranda-apartments-winter-haven-florida.jpg | Jacaranda Apartments, Winter Haven, Florida (postal) | Boston Public Library, Tichnor Bros. collection, via Flickr | CC BY 2.0 |
| assets/sierra-court-motel-winter-haven-florida.jpg | Sierra Court Motel, Winter Haven, Florida (postal) | Boston Public Library, via Flickr | CC BY 2.0 |
| assets/cypress-gardens-florida-26975314327.jpg | Cypress Gardens, Florida (barco no canal) | Mike McBey, via Wikimedia Commons | CC BY 2.0 |
| assets/cypress-gardens-41115552574.jpg | Cypress Gardens (jardins e coreto) | Mike McBey, via Wikimedia Commons | CC BY 2.0 |
| assets/florida-citrus-queen-sally-ardrey-and-her.jpg | Florida Citrus Queen e sua corte, Florida Citrus Exposition, Winter Haven, 1955 | Florida Memory, via Wikimedia Commons | Sem restrições de copyright conhecidas |
| assets/the-orange-blossom-special-going-through-orange.jpg | The Orange Blossom Special going through orange groves in Florida (postal) | Boston Public Library, via Flickr | CC BY 2.0 |
| assets/map/*.png | Tiles do mapa de contato | © OpenStreetMap contributors | ODbL |
| assets/data/lakes.json | Contornos dos lagos (mapa da home e motivo do site) | © OpenStreetMap contributors | ODbL |

Os desenhos dos serviços (dente, coroa, faceta, implante, aparelho de apneia, dente com raio) são SVG feitos para a página e podem ser trocados por fotos reais do consultório.

## Arquivos

- `index.html` e as outras cinco páginas, `styles.css`, `main.js`: o site. Duas fontes (Fraunces e Hanken Grotesk, Google Fonts), sem frameworks, sem build obrigatório.
- `build.py`: gera as seis páginas. `assets/data/lakes.json`: contornos dos lagos e o motivo.
- `assets/`: fotos, tiles do mapa, créditos.
