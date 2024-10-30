from settings import *

async def teams_advanced(page, url):
    await page.goto(url)

    table_entries = page.locator("tbody.Crom_body__UYOcU").locator("tr")
    num_entries = await table_entries.count()

    all_teams_advanced_data = []

    for i in range(num_entries):
        team_advanced_data = {}
        for j in range(len(HEADERS['teams_advanced'])):
            team_advanced_data[HEADERS['teams_advanced'][j]] = await table_entries.nth(i).locator('td').nth(j+1).inner_text()
        all_teams_advanced_data.append(team_advanced_data)

    TEAMS_ADVANCED.insert_many(all_teams_advanced_data)

async def players_advanced(page, url):
    await page.goto(url)
    await page.locator("div.DropDown_dropdown__TMlAR").locator("select.DropDown_select__4pIg9").nth(-1).select_option("All")

    table_entries = page.locator("tbody.Crom_body__UYOcU").locator("tr")
    num_entries = await table_entries.count()

    all_players_advanced_data = []

    for i in range(num_entries):
        player_advanced_data = {}
        for j in range(len(HEADERS['players_advanced'])):
            player_advanced_data[HEADERS['players_advanced'][j]] = await table_entries.nth(i).locator('td').nth(j+1).inner_text()
        all_players_advanced_data.append(player_advanced_data)

    PLAYERS_ADVANCED.insert_many(all_players_advanced_data)

async def players_traditional(page ,url):
    await page.goto(url)
    await page.locator("div.DropDown_dropdown__TMlAR").locator("select.DropDown_select__4pIg9").nth(-1).select_option("All")

    table_entries = page.locator("tbody.Crom_body__UYOcU").locator("tr")
    num_entries = await table_entries.count()

    all_players_traditional_data = []


    for i in range(num_entries):
        player_data = {}
        for j in range(len(HEADERS['players_traditional'])):
            player_data[HEADERS['players_traditional'][j]] = await table_entries.nth(i).locator('td').nth(j+1).inner_text()
        all_players_traditional_data.append(player_data)

    PLAYERS_TRADITIONAL.insert_many(all_players_traditional_data)

FETCH_FUNC = {
    'players_traditional': players_traditional,
    'players_advanced': players_advanced,
    'teams_advanced': teams_advanced
}