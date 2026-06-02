const perguntas = [
    {
        pergunta: 'O que representa uma variável em Python?',
        opcoes: [
            'A) Um valor fixo que nunca muda',
            'B) Um espaço de memória que armazena dados',
            'C) Um comando para repetir instruções',
            'D) Um tipo especial de função'
        ],
        resposta: 'B',
        explicacao: 'Uma variável é um nome que referencia um valor armazenado na memória.'
    },
    {
        pergunta: 'Qual operador usamos para concatenar duas strings em Python?',
        opcoes: ['A) +', 'B) -', 'C) *', 'D) /'],
        resposta: 'A',
        explicacao: 'O operador + une strings, como "Olá" + " Mundo" = "Olá Mundo".'
    },
    {
        pergunta: 'O que o comando for i in range(5): faz?',
        opcoes: [
            'A) Cria uma lista com 5 elementos',
            'B) Repete o bloco 5 vezes com i de 0 a 4',
            'C) Soma 5 ao valor de i',
            'D) Interrompe o programa após 5 segundos'
        ],
        resposta: 'B',
        explicacao: 'range(5) gera valores de 0 a 4 e o for repete o bloco para cada valor.'
    },
    {
        pergunta: 'Qual é o resultado de x = 10; if x % 2 == 0: print(\'par\') else: print(\'ímpar\')?',
        opcoes: ['A) par', 'B) ímpar', 'C) 10', 'D) Nenhuma das anteriores'],
        resposta: 'A',
        explicacao: '10 é divisível por 2, então o programa imprime "par".'
    },
    {
        pergunta: 'Como você define uma função que retorna a soma de dois valores?',
        opcoes: [
            'A) def soma(a, b): return a + b',
            'B) function soma(a, b) { a + b }',
            'C) soma = a + b',
            'D) def soma(a, b): print(a + b)'
        ],
        resposta: 'A',
        explicacao: 'A forma correta em Python é usar def e return para devolver o resultado.'
    },
    {
        pergunta: 'Qual método adiciona um item ao final de uma lista em Python?',
        opcoes: ['A) append', 'B) pop', 'C) remove', 'D) clear'],
        resposta: 'A',
        explicacao: 'append adiciona um elemento ao final da lista.'
    },
    {
        pergunta: 'Qual símbolo começa um comentário em Python?',
        opcoes: ['A) //', 'B) #', 'C) /*', 'D) --'],
        resposta: 'B',
        explicacao: 'O símbolo # inicia um comentário em Python.'
    },
    {
        pergunta: 'Qual tipo de dado representa verdadeiro ou falso?',
        opcoes: ['A) int', 'B) str', 'C) float', 'D) bool'],
        resposta: 'D',
        explicacao: 'bool representa valores booleanos: True ou False.'
    },
    {
        pergunta: 'Qual comando cria um dicionário vazio?',
        opcoes: ['A) []', 'B) {}', 'C) ()', 'D) dict[]'],
        resposta: 'B',
        explicacao: 'Um dicionário vazio é criado com chaves { }.'
    },
    {
        pergunta: 'Como você converte a string "42" para número inteiro?',
        opcoes: ['A) int("42")', 'B) str("42")', 'C) float("42")', 'D) bool("42")'],
        resposta: 'A',
        explicacao: 'A função int converte texto para inteiro quando o texto contém um número válido.'
    },
    {
        pergunta: 'O que faz o método len(lista)?',
        opcoes: ['A) Soma os elementos', 'B) Retorna o tamanho', 'C) Apaga a lista', 'D) Ordena a lista'],
        resposta: 'B',
        explicacao: 'len retorna a quantidade de elementos em uma sequência ou coleção.'
    },
    {
        pergunta: 'Qual instrução é usada para criar uma condição em Python?',
        opcoes: ['A) for', 'B) def', 'C) if', 'D) while'],
        resposta: 'C',
        explicacao: 'if é usado para testar uma condição e executar código condicionalmente.'
    }
];

const startButton = document.getElementById('start-button');
const quizCard = document.getElementById('quiz-card');
const resultCard = document.getElementById('result-card');
const questionTitle = document.getElementById('question-title');
const optionsList = document.getElementById('options-list');
const feedback = document.getElementById('feedback');
const progressText = document.getElementById('progress-text');
const scoreText = document.getElementById('score-text');
const answerButton = document.getElementById('answer-button');
const nextButton = document.getElementById('next-button');
const restartButton = document.getElementById('restart-button');
const resultMessage = document.getElementById('result-message');

let currentIndex = 0;
let score = 0;
let selectedOption = null;

function iniciarQuiz() {
    startButton.closest('.hero-card').classList.add('hidden');
    quizCard.classList.remove('hidden');
    atualizarPergunta();
}

function atualizarPergunta() {
    const pergunta = perguntas[currentIndex];
    questionTitle.textContent = pergunta.pergunta;
    progressText.textContent = `Pergunta ${currentIndex + 1} de ${perguntas.length}`;
    scoreText.textContent = `Pontuação: ${score}`;
    feedback.textContent = 'Escolha uma opção e clique em responder.';
    feedback.style.color = '#475569';
    answerButton.disabled = false;
    answerButton.classList.remove('disabled');
    nextButton.disabled = true;
    nextButton.classList.add('disabled');
    selectedOption = null;
    optionsList.innerHTML = '';

    perguntas[currentIndex].opcoes.forEach((texto, index) => {
        const optionCard = document.createElement('button');
        optionCard.type = 'button';
        optionCard.className = 'option-card';
        optionCard.innerHTML = `<span class="option-label">${texto}</span><span class="option-radio"></span>`;
        optionCard.addEventListener('click', () => selecionarOpcao(optionCard, index));
        optionsList.appendChild(optionCard);
    });
}

function selecionarOpcao(card, index) {
    const cards = document.querySelectorAll('.option-card');
    cards.forEach(item => item.classList.remove('selected'));
    card.classList.add('selected');
    selectedOption = perguntas[currentIndex].opcoes[index].charAt(0);
}

function validarResposta() {
    if (!selectedOption) {
        feedback.textContent = 'Por favor, selecione uma resposta antes de continuar.';
        feedback.style.color = '#b91c1c';
        return;
    }

    const pergunta = perguntas[currentIndex];
    const respostaCorreta = pergunta.resposta;
    if (selectedOption === respostaCorreta) {
        score += 1;
        feedback.textContent = `✅ Correto! ${pergunta.explicacao}`;
        feedback.style.color = '#0f766e';
    } else {
        feedback.textContent = `❌ Errado. A resposta correta é ${respostaCorreta}. ${pergunta.explicacao}`;
        feedback.style.color = '#b91c1c';
    }

    scoreText.textContent = `Pontuação: ${score}`;
    answerButton.disabled = true;
    answerButton.classList.add('disabled');
    nextButton.disabled = false;
    nextButton.classList.remove('disabled');
}

function proximaPergunta() {
    currentIndex += 1;
    if (currentIndex >= perguntas.length) {
        terminarQuiz();
    } else {
        atualizarPergunta();
    }
}

function terminarQuiz() {
    quizCard.classList.add('hidden');
    resultCard.classList.remove('hidden');
    resultMessage.textContent = `Você acertou ${score} de ${perguntas.length} perguntas. Continue praticando para melhorar ainda mais!`;
}

function reiniciarQuiz() {
    currentIndex = 0;
    score = 0;
    resultCard.classList.add('hidden');
    quizCard.classList.remove('hidden');
    atualizarPergunta();
}

startButton.addEventListener('click', iniciarQuiz);
answerButton.addEventListener('click', validarResposta);
nextButton.addEventListener('click', proximaPergunta);
restartButton.addEventListener('click', reiniciarQuiz);
