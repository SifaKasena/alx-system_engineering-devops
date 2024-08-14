# Debug Wordpress site
exec { 'Fix typo':
  command => 'sed -i s/phpp/php/ /var/www/html/wp-settings.php',
  path    => '/usr/bin:/usr/sbin:/bin'
}
