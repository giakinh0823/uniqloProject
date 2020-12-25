window.parent.postMessage("resize", "*");

const slideWidth = 1024;
const slider = document.querySelector('.carousel--slider-container');
const wrapper = slider.querySelector('.carousel--slider-wrapper');
const slides = slider.querySelectorAll('.carousel--slide');
const indicators = slider.querySelectorAll('.carousel--slider--indicators a');
const controls = document.querySelector('.carousel--slider--controls');
let isPlaying = true;

document.addEventListener('DOMContentLoaded', $ => {
  controls.querySelector('.previous').addEventListener('click', prevSlide);
  controls.querySelector('.next').addEventListener('click', nextSlide);

  indicators.forEach(indicator => {
    indicator.addEventListener('click', jumpTo);
  });

  setResetInterval(isPlaying);
  controls.querySelector('.carousel--slider--control_toggle').addEventListener('change', e => {
    setResetInterval(e.target.checked);

    const icon = controls.querySelector('i.fa');
    if (e.target.checked) {
      icon.classList.add('fa-pause');
      icon.classList.remove('fa-play');
    } else {
      icon.classList.remove('fa-pause');
      icon.classList.add('fa-play');
    }
  });

});

const nextSlide = () => {
  const activeBox = slider.querySelector('.carousel--slide .carousel--box-wrapper.active');
  const activeSlide = activeBox.parentElement;
  const next = activeBox.parentElement.nextElementSibling ?
  activeBox.parentElement.nextElementSibling.querySelector('.carousel--box-wrapper') :
  slides[0].querySelector('.carousel--box-wrapper');
  const wrapperMargin = parseInt(wrapper.style.marginLeft.replace('px', ''));

  wrapper.style.marginLeft = activeBox.parentElement.nextElementSibling ?
  `${wrapperMargin - slideWidth}px` : 0;

  activeBox.classList.remove('active');
  next.classList.add('active');

  const nodes = Array.prototype.slice.call(slides);
  const index = nodes.indexOf(activeSlide) + 1;
  const indicators = document.querySelectorAll('.carousel--slider--indicators li a');
  indicators.forEach(indicator => {
    indicator.classList.remove('active');
  });

  const targetIndicator = indicators[index] ? indicators[index] : indicators[0];
  targetIndicator.classList.add('active');
};

const prevSlide = () => {
  const activeBox = slider.querySelector('.carousel--slide .carousel--box-wrapper.active');
  const activeSlide = activeBox.parentElement;
  const prev = activeBox.parentElement.previousElementSibling ?
  activeBox.parentElement.previousElementSibling.querySelector('.carousel--box-wrapper') :
  slides[slides.length - 1].querySelector('.carousel--box-wrapper');
  const wrapperMargin = parseInt(wrapper.style.marginLeft.replace('px', ''));

  wrapper.style.marginLeft = activeBox.parentElement.previousElementSibling ?
  `${wrapperMargin + slideWidth}px` :
  `${-1 * (slideWidth * (slides.length - 1))}px`;

  activeBox.classList.remove('active');
  prev.classList.add('active');

  const nodes = Array.prototype.slice.call(slides);
  const index = nodes.indexOf(activeSlide) - 1;
  const indicators = document.querySelectorAll('.carousel--slider--indicators li a');
  indicators.forEach(indicator => {
    indicator.classList.remove('active');
  });

  const targetIndicator = indicators[index] ? indicators[index] : indicators[indicators.length - 1];
  targetIndicator.classList.add('active');
};

const jumpTo = slide => {
  slide.preventDefault();
  indicators.forEach(indicator => {
    indicator.classList.remove('active');
  });

  const parentLink = slide.target.closest('a');
  parentLink.classList.add('active');

  const rel = parentLink.getAttribute('rel');
  const index = rel.replace('step', '') - 1;

  slides.forEach(slide => {
    slide.querySelector('.carousel--box-wrapper').classList.remove('active');
  });

  wrapper.style.marginLeft = `${-1 * index * slideWidth}px`;
  slides[index].querySelector('.carousel--box-wrapper').classList.add('active');
};

const setResetInterval = isActive => {
  const slideSpeed = 4500;
  const slidesLength = slides.length;
  let i = 0;

  if (isActive) {
    timer = setInterval(function () {
      // console.log('shift!');

      setTimeout(function () {
        nextSlide();
        // console.log('timeout');
        // insert cycle animation here
      }, 3000);
    }, slideSpeed);
  } else {
    clearInterval(timer);
  }
};

document.addEventListener('keyup', e => {
  if (e.defaultPrevented) {
    return;
  }

  // only slide if slider is in viewport;
  let bounding = slider.getBoundingClientRect();
  if (
  bounding.top >= 0 &&
  bounding.left >= 0 &&
  bounding.right <= (window.innerWidth || document.documentElement.clientWidth) &&
  bounding.bottom <= (window.innerHeight || document.documentElement.clientHeight))
  {
    if (e.keyCode === 37) {
      prevSlide();
    } else if (e.keyCode === 39) {
      nextSlide();
    }
  } else {
    return;
  }
});
//# sourceURL=pen.js











