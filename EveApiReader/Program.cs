using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using System;
using read_memory_64_bit;

var builder = WebApplication.CreateBuilder(args);

var app = builder.Build();

// --- Убрано всё, связанное с HTTPS ---

var lifetime = app.Services.GetRequiredService<IHostApplicationLifetime>();

lifetime.ApplicationStopping.Register(() =>
{
    Console.WriteLine("[EveApiReader] Приложение останавливается. Очищаем кэши EveModuleReader...");
    try
    {
        EveModuleReader.DisposeAllCaches();
        Console.WriteLine("[EveApiReader] Кэши EveModuleReader успешно очищены.");
    }
    catch (Exception ex)
    {
        Console.Error.WriteLine($"[EveApiReader] Ошибка при очистке кэшей EveModuleReader: {ex.GetType().Name} - {ex.Message}");
    }
});

// --- Маршруты остаются без изменений ---
app.MapGet("/api/eve/quantity/{pid:int}", (int pid) =>
{
    app.Logger.LogInformation("[EveApiReader] Получен запрос для PID: {ProcessId}", pid);
    try
    {
        long? quantity = EveModuleReader.GetModuleQuantity(pid);

        if (quantity.HasValue)
        {
            app.Logger.LogInformation("[EveApiReader] Успешно получено quantity={Quantity} для PID: {ProcessId}", quantity.Value, pid);
            return Results.Ok(new { quantity = quantity.Value });
        }
        else
        {
            app.Logger.LogError("[EveApiReader] Не удалось получить quantity для PID: {ProcessId} (GetModuleQuantity вернул null).", pid);
            return Results.NotFound(new { error = $"Не найдены данные для quantity у процесса с PID {pid}." });
        }
    }
    catch (InvalidOperationException ex)
    {
        app.Logger.LogError(ex, "[EveApiReader] Ошибка чтения данных для PID {ProcessId}", pid);
        return Results.Problem(
            detail: $"Ошибка чтения данных для PID {pid}: {ex.Message}",
            statusCode: StatusCodes.Status500InternalServerError,
            title: "Ошибка чтения данных EVE");
    }
    catch (Exception ex)
    {
        app.Logger.LogError(ex, "[EveApiReader] Необработанная ошибка для PID {ProcessId}", pid);
        return Results.Problem(
            detail: $"Необработанная ошибка при запросе PID {pid}: {ex.Message}",
            statusCode: StatusCodes.Status500InternalServerError,
            title: "Необработанная ошибка сервера");
    }
});

app.MapGet("/", () => Results.Ok("Eve API Reader is running (HTTP only)!"));

app.Logger.LogInformation("[EveApiReader] Веб-сервис запущен...");

// Убедитесь, что приложение слушает только HTTP порт
app.Run("http://localhost:5052"); // Явно указываем HTTP порт