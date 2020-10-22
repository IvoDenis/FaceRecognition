using System;
using System.Collections.Generic;
using System.Linq;
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
            var client = new MongoClient(settings.ConnectionString);
            var database = client.GetDatabase(settings.DatabaseName);
            _employers = database.GetCollection<Employer>(settings.EmployersCollectionName);
        }
        public List<Employer> Get()
        {
           return _employers.Find(p => true).ToList();
        }
        public async Task Remove(string id)
        {
           await _employers.DeleteOneAsync(emp => (emp.Id == id));
        }
        public async Task Add(Employer employer)
        {
            await _employers.InsertOneAsync(employer);
        }
   
        public async Task Update(Employer employer)
        {
            await _employers.ReplaceOneAsync(new BsonDocument("_id",new ObjectId(employer.Id)), employer);
        }



    }
}
