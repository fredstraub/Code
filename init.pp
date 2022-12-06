# Create two users.
$users = ['user1', 'user2']

user { $users:
  ensure  => present,
  groups  => ['my_group']
}

# Create group.
group { 'my_group':
  ensure => present
}

# Install packages.
package {'pip3':
  require  => Package['python3-pip'],
  ensure   => installed,
  provider => 'pip3'
}

package { ['python3-pip']:
  ensure => installed
}

package {'apache2':
  ensure => installed
}

package { 'libapache2-mod-wsgi':
  ensure  => installed
}

package { 'bottle':
  ensure   => '0.10.11',
  provider => 'pip3'
}
