using Microsoft.AspNetCore.Mvc;

namespace UserLoginApp.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            if (string.IsNullOrEmpty(HttpContext.Session.GetString("User")))
            {
                return RedirectToAction("Login", "Account");
            }

            ViewBag.User = HttpContext.Session.GetString("User");
            return View();
        }
    }
}
