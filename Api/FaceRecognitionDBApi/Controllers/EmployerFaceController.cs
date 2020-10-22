using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using FaceRecognitionDBApi.Services;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.DependencyInjection;
using Newtonsoft.Json;

namespace FaceRecognitionDBApi.Controllers
{
    [Route("/employers")]
    [ApiController]
    public class EmployerFaceController : ControllerBase
    {
        private EmployerService _employerService;

        public EmployerFaceController(EmployerService employerService)
        {
            _employerService = employerService;
        }

        // GET: /employers
        [HttpGet]

        public IEnumerable<Employer> Get()
        {
            return _employerService.Get();
        }


        // POST: /employers
        [HttpPost]
        public async Task Post([FromBody] Employer employer)
        {

            await _employerService.Add(employer);

        }

        // PUT: employers/
        [HttpPut]
        public async Task Put([FromBody] Employer employer)
        {
            await _employerService.Update(employer);
        }

        // DELETE: employers/id
        [HttpDelete("{id}")]
        public async Task Delete(string id)
        {
            await _employerService.Remove(id);
        }
    }
}
