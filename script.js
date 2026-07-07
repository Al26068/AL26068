// ==============================
// 写真を追加する時はここだけ編集！
// ==============================
const slides = [
    {
        file: 'hongkong1.png',
        name: '香港 Victoria Peak',
        mapUrl: 'https://maps.google.com/?q=Victoria+Peak,Hong+Kong'
    },
    {
        file: 'hongkong2.png',
        name: '香港 Sham Shui Po',
        mapUrl:'https://maps.app.goo.gl/pG7fDTU9SMS9iR3t8'
    },
    {
        file: 'shibuya1.png',
        name: '日本 Shibuya scramble cross',
        mapUrl:'https://maps.app.goo.gl/jTJUrkpdgGuF1q1S9'
    },
    {
        file: 'hongkong3.png',
        name: '香港 Shek Tong Tsui',
        mapUrl: 'https://maps.app.goo.gl/tbUStMNLL4q7X3aY6'
    }
    // 写真追加例↓（コピペして使ってね）
    // {
    //     file: '写真2.jpg',
    //     name: '渋谷 スクランブル交差点',
    //     mapUrl: 'https://maps.google.com/?q=Shibuya+Scramble+Crossing,Tokyo'
    // },
];

// スライドショー初期化
function initSlideshow() {
    if (slides.length <= 1) return; // 写真1枚なら切り替えなし

    const container = document.getElementById('bgSlideshow');
    const label = document.getElementById('locationLabel');
    const nameEl = label.querySelector('.loc-name');
    const linkEl = label.querySelector('.loc-link');

    // HTMLのスライドdivを動的に生成（slides配列から）
    container.innerHTML = '';
    slides.forEach((s, i) => {
        const div = document.createElement('div');
        div.className = 'bg-slide' + (i === 0 ? ' active' : '');
        div.style.backgroundImage = `url('${s.file}')`;
        container.appendChild(div);
    });

    let current = 0;
    const divs = container.querySelectorAll('.bg-slide');

    function goTo(next) {
        // ラベルをフェードアウト
        label.classList.remove('visible');

        setTimeout(() => {
            divs[current].classList.remove('active');
            current = next;
            divs[current].classList.add('active');

            // ラベル更新してフェードイン
            nameEl.textContent = slides[current].name;
            linkEl.href = slides[current].mapUrl;
            label.classList.add('visible');
        }, 1000);
    }

    // 6秒ごとに切り替え
    setInterval(() => {
        goTo((current + 1) % slides.length);
    }, 6000);
}

document.addEventListener('DOMContentLoaded', () => {
    initSlideshow();
});

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

/*window.onload = () => {
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
*/