with sources as (
    select *
    from
    {{source('poke_pg_dbt','pokemon_abilities')}}
)

SELECT 
    id,
    raw_id,
    user_id,
    pokemon_ability_id,
    regexp_replace(language::json ->> 'url', '.*/([0-9]+)/$', '\1')::int as language_id,
    effect,
    short_effect
 FROM Sources