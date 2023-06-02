import { Ball } from './ball'
export class App {
    constructor () {
        this.canvas = document.createElement("canvas")
        this.ctx = this.canvas.getContext("2d");
        document.body.appendChild(this.canvas)
        // resize 이벤트 바생시 resize 메소드에 window 객체를 this로서 할당
        window.addEventListener('resize', this.resize.bind(this), false)
        this.resize()

        this.ball = new Ball({stage: this.stage, radius: 60, speed: 15})

        // 다음 리페인트에서 그 다음 프레임을 애니메이트하려면 콜백 루틴이 반드시 스스로 
        // requestAnimationFrame()을 호출해야합니다.
        // 화면에 새로운 애니메이션을 업데이트할 준비가 될때마다 이 메소드를 호출하는것이 좋습니다
        window.requestAnimationFrame(this.animate.bind(this))

    }
    resize () {
        this.stage = {
            w: document.body.clientWidth,
            h: document.body.clientHeight
        }
        this.canvas.width = this.stage.w * 2
        this.canvas.height = this.stage.h * 2
        this.ctx.scale(2, 2)
    }
    animate(t) {
        window.requestAnimationFrame(this.animate.bind(this))
        this.ctx.clearRect(0, 0, this.stage.w, this.stage.y)
        this.ball.draw(this.ctx, stage)
    }
}
window.onload = () => {
    new App()
}