// ===========================
// Menús de 3 punticos para tarjetas y para "crear nuevo"
// ===========================
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".card-options-btn").forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      e.stopPropagation();
      // Cierra otros menús abiertos
      document
        .querySelectorAll(".card-options-menu.show")
        .forEach(function (menu) {
          menu.classList.remove("show");
        });
      // Abre el menú de este botón
      var menu = btn
        .closest(".menu-container")
        .querySelector(".card-options-menu");
      if (menu) menu.classList.toggle("show");
    });
  });
  // Cierra el menú si se hace clic fuera
  document.body.addEventListener("click", function () {
    document
      .querySelectorAll(".card-options-menu.show")
      .forEach(function (menu) {
        menu.classList.remove("show");
      });
  });
});
