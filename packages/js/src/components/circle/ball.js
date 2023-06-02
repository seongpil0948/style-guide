export class Ball {
    constructor ({stage, radius, speed}) {
        this.radius = radius
        this.vx = speed
        this.vy = speed
        const diameter = this.radius * 2
        // 공이 스테이지에 랜덤으로 위치
        this.x = diameter + (Math.random() * stage.w - diameter)
        this.y = diameter + (Math.random() * stage.y - diameter)
    }
    draw(ctx, stage) {
        this.x += this.vx
        this.y += this.vy

        this.bounceWindow(stage)
        ctx.fillStyle("#fdd700")
        ctx.beginPath()
        ctx.arc(this.x, this.y, this.radius, 0,  2 * Math.PI)
        ctx.fill()
    }
    bounceWindow(stage) {
        const minX = this.radius
        const maxX = stage.w - this.radius
        const minY = this.radius
        const maxY = stage.y - this.radius

        if (this.x <= minX || this.x >= maxX) {
            this.vx *= -1
            this.x += this.vx
        } else if (this.y <= minY || this.y >= maxY) {
            this.vy *= -1
            this.y += this.vy
        }
    }
}