from selection_stats import get_stats_by_event_id, get_full_selection_stats

selections = ['13040758', '13040759', '13040760']

d = get_full_selection_stats(selections)
print(d)