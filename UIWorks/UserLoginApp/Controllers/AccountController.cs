using Microsoft.AspNetCore.Mvc;
using UserLoginApp.Models;
using Microsoft.AspNetCore.Http;

namespace UserLoginApp.Controllers
{
    public class AccountController : Controller
    {
        private const string ValidUsername = "user";
        private const string ValidPassword = "pass";

        public IActionResult Login()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Login(LoginViewModel model)
        {
            if (model.Username == ValidUsername && model.Password == ValidPassword)
            {
                HttpContext.Session.SetString("User", model.Username);
                return RedirectToAction("Index", "Home");
            }

            ViewBag.Error = "Invalid credentials";
            return View();
        }

        public IActionResult Logout()
        {
            HttpContext.Session.Clear();
            return RedirectToAction("Login");
        }
    }
}
