//言語変更モジュール
 function changeLang(lang){ 
   const elements = document.querySelectorAll("[data-ja]");

   elements.forEach(el => {
      const text = el.getAttribute(`data-${lang}`);
      if (text) {
         el.innerHTML = text;
      }
   })
   };

window.onload = () => {
//流れ星陣営

setInterval(() => {

  const star = document.createElement("div");
  star.className = "shooting-star";

  // 位置
  star.style.top = Math.random() * window.innerHeight + "px";
  star.style.left = Math.random() *window.innerWidth + "px";

  // 色
  const r = Math.random() * 100;
  let color;

  if (r < 2) color = "#ff4d4d";
  else if (r < 7) color = "#ffa500";
  else if (r < 9) color = "#ffff66";
  else if (r < 19) color = "#ccf2ff";
  else color = "#ffffff";

  star.style.background = `linear-gradient(${color}, transparent)`;
  star.style.boxShadow = `0 0 10px ${color}`;

  document.body.appendChild(star);

  setTimeout(() => {
    star.remove();
  }, 1000); // ← CSSのanimationと合わせる

}, 1000);

// 背景の星陣営
for (let i = 0; i < 800; i++) {
        const star = document.createElement("div");
        star.className = "star";

        const rand = Math.random();
         if(rand < 0.33){
            star.classList.add("small");
         } else if (rand<0.66) {
            star.classList.add("medium");
         } else {
            star.classList.add("big");
         }
         


        star.style.top = Math.random() * window.innerHeight * 3 + "px";
        star.style.left = Math.random() * window.innerWidth + "px";

        const r = Math.random() * 100;
         let color;
         if (r < 2) {color = "#ff4d4d";}
         else if (r < 7) {color = "#ffa500";}
         else if (r < 9) {color = "#ffff66";}
         else if (r < 19) {color = "#ccf2ff";}
         else {color = "#ffffff";}
         
         star.style.background = color;
         star.style.boxShadow = `0 0 6px ${color}`;
         
        const size = Math.random() * 3 + 1;
        star.style.width = size + "px";
        star.style.height = size + "px";

        document.body.appendChild(star);
    }


}