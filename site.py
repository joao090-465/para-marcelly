from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Para Marcelly</title>
        <style>
            body {
                background-color: #05020a;
                color: #ffffff;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                overflow: hidden;
            }
            #conteudoPrincipal {
                text-align: center;
                animation: fadeIn 1.5s ease-in-out;
            }
            h1 { 
                color: #bc6ff1; 
                font-size: 38px;
                margin-bottom: 30px; 
                font-weight: 600;
                letter-spacing: 2px;
                text-shadow: 0 0 15px rgba(188, 111, 241, 0.6);
            }
            button {
                background: transparent;
                color: #bc6ff1;
                border: 2px solid #bc6ff1;
                padding: 15px 35px;
                font-size: 18px;
                font-weight: bold;
                cursor: pointer;
                border-radius: 30px;
                transition: all 0.4s ease;
                box-shadow: 0 0 15px rgba(188, 111, 241, 0.2);
                letter-spacing: 1px;
            }
            button:hover {
                background: #bc6ff1;
                color: #05020a;
                box-shadow: 0 0 30px rgba(188, 111, 241, 0.8);
                transform: scale(1.05);
            }
            #telaAnimacao {
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw;
                height: 100vh;
                background-color: #030106;
                display: none;
            }
            canvas {
                width: 100%;
                height: 100%;
                position: absolute;
                top: 0;
                left: 0;
            }
            #caixaTexto {
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                text-align: center;
                width: 85%;
                max-width: 600px;
                display: none;
                opacity: 0;
                transition: opacity 2.5s ease-in-out;
                z-index: 10;
                background: rgba(5, 2, 10, 0.85);
                padding: 30px;
                border-radius: 20px;
                backdrop-filter: blur(5px);
                border: 1px solid rgba(188, 111, 241, 0.2);
            }
            .mensagem {
                font-size: 22px;
                line-height: 1.6;
                color: #f3e8ff;
                margin-bottom: 25px;
                font-family: 'Georgia', serif;
                font-style: italic;
                text-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
            }
            .assinatura {
                font-size: 28px;
                font-weight: bold;
                color: #ffffff;
                text-shadow: 0 0 15px rgba(188, 111, 241, 0.6);
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(20px); }
                to { opacity: 1; transform: translateY(0); }
            }
        </style>
    </head>
    <body>
        <div id="conteudoPrincipal">
            <h1>Perdão por tudo...</h1>
            <button onclick="iniciarSurpresa()">Abrir de Coração</button>
        </div>
        <div id="telaAnimacao">
            <canvas id="canvasCoracao"></canvas>
            <div id="caixaTexto">
                <p class="mensagem">
                    "Marce, eu sei que às vezes sou ignorante e chato, e te peço desculpas por isso do fundo do meu coração... Mas eu quero que você saiba o quanto eu te amo e o quanto você é importante para mim."
                </p>
                <p class="assinatura">Eu Amo Você</p>
            </div>
        </div>
        <script>
            function iniciarSurpresa() {
                document.getElementById('conteudoPrincipal').style.display = 'none';
                const tela = document.getElementById('telaAnimacao');
                tela.style.display = 'block';
                const canvas = document.getElementById('canvasCoracao');
                const ctx = canvas.getContext('2d');
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
                const cx = canvas.width / 2;
                const cy = canvas.height / 2;
                const coresNeon = ["#9b5de5", "#ba55d3", "#da70d6", "#ee82ee", "#dda0dd"];
                const textosOpcoes = ["Love you", "I love you", "LOVE YOU", "Marcelly"];
                let pontosValidos = [];
                const tamanhoEscala = Math.min(canvas.width, canvas.height) / 55;
                function dentroDoCoracao(x, y) {
                    const nx = (x - cx) / tamanhoEscala;
                    const ny = -(y - cy) / tamanhoEscala;
                    return Math.pow(nx*nx + ny*ny - 1, 3) - (nx*nx) * Math.pow(ny, 3) <= 0;
                }
                const raioBusca = tamanhoEscala * 20;
                for (let y = cy - raioBusca; y < cy + raioBusca; y += 15) {
                    for (let x = cx - raioBusca; x < cx + raioBusca; x += 34) {
                        if (dentroDoCoracao(x, y)) {
                            const rx = x + (Math.random() * 8 - 4);
                            const ry = y + (Math.random() * 8 - 4);
                            pontosValidos.push({x: rx, y: ry});
                        }
                    }
                }
                pontosValidos.sort((a, b) => a.y - b.y);
                let indice = 0;
                const passoPorFrame = 2; 
                function animar() {
                    for (let i = 0; i < passoPorFrame; i++) {
                        if (indice < pontosValidos.length) {
                            const p = pontosValidos[indice];
                            ctx.fillStyle = coresNeon[Math.floor(Math.random() * coresNeon.length)];
                            const tamFonte = Math.floor(Math.random() * 3) + 9;
                            ctx.font = `bold ${tamFonte}px Arial`;
                            const txt = textosOpcoes[Math.floor(Math.random() * textosOpcoes.length)];
                            ctx.fillText(txt, p.x, p.y);
                            indice++;
                        } else {
                            const caixa = document.getElementById('caixaTexto');
                            caixa.style.display = 'block';
                            setTimeout(() => {
                                caixa.style.opacity = '1';
                            }, 50);
                            return;
                        }
                    }
                    requestAnimationFrame(animar);
                }
                animar();
            }
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    porta = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=porta)
