var owl = $('.caurosel__list--owl');
owl.owlCarousel({
  items: 4,
  loop: true,
  margin: 30,
  responsiveClass: true,
  URLhashListener:true,
  lazyLoadEager:true,
  autoHeight: true,
  nav: true,
  autoplay:true,
  autoplayTimeout:5000,
    responsive:{
    0:{
        items:1
    },
    600:{
        items:2
    },            
    960:{
        items:3
    },
    1200:{
        items:4
    },
    scrollPerPage: true,
    navigation: true
}
});
// owl.on('mousewheel', '.owl-stage', function (e) {
//   if (e.deltaY > 0) {
//     owl.trigger('next.owl');
//   } else {
//     owl.trigger('prev.owl');
//   }
//   e.preventDefault();
// });




