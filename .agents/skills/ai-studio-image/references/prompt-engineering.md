# Engenharia de Prompts para Imagens Humanizadas

A diferenca fundamental entre uma imagem gerada por IA generica e uma fotografia real reside nos detalhes e imperfeicoes naturais do mundo fisico.

---

## As 5 Camadas de Humanizacao de Prompts

```text
┌─────────────────────────────────────────────────────────────┐
│                 Prompt Base do Usuario                      │
└──────────────────────────────┬──────────────────────────────┘
                               │
       ┌───────────────────────┼───────────────────────┐
       ▼                       ▼                       ▼
┌──────────────┐        ┌──────────────┐        ┌──────────────┐
│Camada 1:     │        │Camada 2:     │        │Camada 3:     │
│Dispositivo   │        │Iluminacao    │        │Imperfeicoes  │
│Smartphone    │        │Natural/Janela│        │Assimetria/ISO│
└──────┬───────┘        └──────┬───────┘        └──────────────┘
       │                       │
       ▼                       ▼
┌──────────────┐        ┌──────────────┐
│Camada 4:     │        │Camada 5:     │
│Autenticidade │        │Contexto      │
│Pele real/Poro│        │Ambiente vivo │
└──────────────┘        └──────────────┘
```

### Camada 1: Dispositivo e Tecnica Fotografica
- **Estilo de captura:** Foto casual tirada com camera de smartphone moderno (iPhone / Samsung Galaxy flagship).
- **Optica:** Lente de 24mm/28mm equivalente, profundidade de campo organica, bokeh suave de lente compacta.
- **Sem flash artificial:** Luz ambiente do local sem iluminacao de estudio.

### Camada 2: Iluminacao Natural e Direcional
- **Fontes organicas:** Luz indireta de janela, raios suaves de *golden hour*, luz difusa em dias nublados ou iluminacao quente de interiores de cafeteria.
- **Sombras suaves:** Gradientes de sombra realistas e reflexos sutis em superficies metalicas/vidro.

### Camada 3: Imperfeicoes Humanas e Opticas
- **Enquadramento descentralizado:** Composicao espontanea, nao perfeitamente simetrica.
- **Granulacao sutil (ISO Noise):** Textura organica de sensor fotografico, especialmente em areas de sombra.
- **Foco seletivo natural:** Elementos secundarios no primeiro ou segundo plano levemente desfocados.

### Camada 4: Autenticidade Humana
- **Textura de pele real:** Poros visiveis, marcas de expressao sutis, sem efeito plastico/porcelana de IA.
- **Expressoes espontaneas:** Olhar natural, sorriso descontraido, expressao focada ou casual (evitando poses rigidas de stock photo).
- **Vestuario organico:** Tecidos com dobras naturais e caimento do dia a dia.

### Camada 5: Contexto e Ambiente Vivo
- **Elementos do cotidiano:** Xicara de cafe com vapor leve, caderno com anotacoes, chaves, plantas ao fundo, reflexos na janela.
- **Cenario coerente:** Locais reais e habitados (cafeteria movimentada, espaco de trabalho real, rua urbana com pedestres desfocados).
