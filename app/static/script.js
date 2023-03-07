$(document).ready(function () {

  // AUTH

  $('.auth__byagrify').show()
  $('.btn--agrify').addClass('auth__button--active')

  $('.btn--one_id').click(function () {
    $('.auth__byoneid').show()
    $('.auth__byagrify').hide()
    $('.btn--agrify').removeClass('auth__button--active')
    $('.btn--one_id').addClass('auth__button--active')
  })

  $('.btn--agrify').click(function () {
    $('.auth__byoneid').hide()
    $('.auth__byagrify').show()
    $('.btn--one_id').removeClass('auth__button--active')
    $('.btn--agrify').addClass('auth__button--active')
  })

  // BARS 

  const $button = document.querySelector('#sidebar-toggle');
  const $wrapper = document.querySelector('#wrapper');

  $button.addEventListener('click', (e) => {
    $('.profile_logo').toggleClass('hide')
    e.preventDefault();
    $wrapper.classList.toggle('toggled');
  });

});
