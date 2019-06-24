ssh admin@bigip.example.com modify auth user admin password cowpigdog
export BIGPASS=cowpigdog
ssh admin@bigip.example.com modify sys provision asm level nominal
ssh admin@bigip.example.com  save sys config
