const addEventOnElements = function (elements, eventType, callback) {
  for (const elem of elements) elem.addEventListener(eventType, callback);
}

const searchBox = document.querySelector("[search-box]");
const searchTogglers = document.querySelectorAll("[search-toggler]");

addEventOnElements(searchTogglers, "click", function () {
  searchBox.classList.toggle("active");
});

const sidebar = document.querySelector("[sidebar]");
const sidebarBtn = document.querySelector("[menu-btn]");
const sidebarTogglers = document.querySelectorAll("[menu-toggler]");
const sidebarClose = document.querySelectorAll("[menu-close]");
const overlay = document.querySelector("[overlay]");

addEventOnElements(sidebarTogglers, "click", function() {
  sidebar.classList.toggle("active");
  sidebarBtn.classList.toggle("active");
  overlay.classList.toggle("active");
});

addEventOnElements(sidebarClose, "click", function() {
  sidebar.classList.remove("active");
  sidebarBtn.classList.remove("active");
  overlay.classList.remove("active");
});

const searchWrapper = document.querySelector("[search-wrapper]");
const searchField = document.querySelector("[search-field]");
const searchForm = document.querySelector("[search-form]");

searchField.addEventListener("input", function() {
  if(!searchField.value.trim()) {
    searchWrapper.classList.remove("searching");
    return;
  }
  searchWrapper.classList.add("searching");

});

searchField.addEventListener("keydown", function(event) {
  if (event.key === "Enter") {
    event.preventDefault(); // Предотвращаем обычное поведение нажатия клавиши Enter
    performSearch();
  }
});

function performSearch() {
  const searchValue = searchField.value.trim();
  if (searchValue !== "") {
    const url = `/search/${encodeURIComponent(searchValue)}`;
    window.location.href = url;
  }
}