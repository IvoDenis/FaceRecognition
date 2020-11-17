using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Authentication;
using System.Threading.Tasks;
using FaceRecognitionDBApi.Models;
using MongoDB.Bson;
using MongoDB.Driver;

namespace FaceRecognitionDBApi.Services
{
    public class EmployerService
    {
        private readonly IMongoCollection<Employer> _employers;
        public EmployerService(IEmployersDatabaseSettings settings)
        {
            MongoClientSettings mongoSettings = MongoClientSettings.FromUrl(
                         new MongoUrl(settings.ConnectionString)
                                                );
            mongoSettings.SslSettings =
              new SslSettings() { EnabledSslProtocols = SslProtocols.Tls12 };
            var client = new MongoClient(mongoSettings);
            var database = client.GetDatabase(settings.DatabaseName);
            _employers = database.GetCollection<Employer>(settings.EmployersCollectionName);
        }
        public async Task<List<Employer>> Get()
        {
            var result = await _employers.FindAsync(p => true);
            return result.ToList();
        }
        public async Task Remove(string id)
        {
            await _employers.DeleteOneAsync(emp => (emp.Id == id));
        }
        public async Task Add(Employer employer)
        {
            await _employers.InsertOneAsync(employer);
        }

        public async Task Update(string id, Employer employer)
        {
            await _employers.ReplaceOneAsync(emp => emp.Id == id, employer);
        }



    }
}
