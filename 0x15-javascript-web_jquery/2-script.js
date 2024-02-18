// Adding an event to the webpage
const redHeader = document.querySelector('DIV#red_header');
const header = document.querySelector('header');
redHeader.addEventListener('click', () => {
  header.style.color = '#FF0000';
});
